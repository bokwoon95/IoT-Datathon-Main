from bs4 import BeautifulSoup as bs
import urllib.request as r
import pandas as pd
import sys
import time

# This function will swap the rows and columns of a 2x2 list
# It uses python's inbuilt zip() function to handle transposition
# However zip() returns a list of tuples instead, so this function will convert that back into a list of lists
def transpose(lol):
    transposedToLot = zip(*lol) #the * asterisk is very important! It prevents zip() from creating a list with a single tuple of tuples
    convertedToLol = [list(x) for x in transposedToLot]
    return list(convertedToLol)

a = "https://www.wunderground.com/history/airport/RCSS/2017/"
b = "/DailyHistory.html?req_city=New+Taipei+City&req_state=TPQ&req_statename=Taiwan&reqdb.zip=00000&reqdb.magic=5&reqdb.wmo=58968"

urls = [] #contains all the urls that we will be accessing

# this loop will populate the url list with the relevant urls
for month in range(5,12):
    if (month==6 or month==9 or month==11):
        for day in range(1,31):
            urls.append(a + str(month) + "/" + str(day) + b)
    else:
        for day in range(1,32):
            urls.append(a + str(month) + "/" + str(day) + b)
print("URLs generated. There %s %d url%s" % ("is" if len(urls)==1 else "are", len(urls), "" if len(urls)==1 else "s."))

#beautifulsoup boilerplate code
opener = r.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

df = pd.DataFrame() #Initialize the dataframe
j = 1
mth = 5
dy = 1
for item in urls:
    html = opener.open(item)
    bsObj = bs(html.read(), "html5lib") #bsObj is a BeautifulSoup Object that contains the entire html file data
    bs_table = bsObj.find("table", {"id":"obsTable"}) #bs_table is a table with the id 'obsTable', extracted from bsObj
    tbl_list = []

    #Go through each bs_table cell with the tag <tr> and copy it into a 2x2 table 'tbl_list'
    for row in bs_table.findAll("tr"):
        tmp_list = [] #tmp_list represents the current row we are building
        for item in row:
            try:
                string = item.get_text().strip()
                s=""
                for c in string:
                    if c.isdigit() or c.isalpha() or c==r"." or c==r" " or c=="(" or c==")" or c==":": #only these characters are allowed
                        s += c
                    else:
                        break #the moment you encounter an invalid character, stop reading and move on to the next item in the row
                tmp_list.append(s)
            except:
                pass
        tbl_list.append(tmp_list)

    # temporarily transpose the columns to become rows so that I can remove the irrelevant columns
    tbl_list = transpose(tbl_list)

    newlist = [] #Because python is acting fucked up, instead of removing all columns that are not "Time", "Temp" or "Humidity" I have to create a new list and append the "Time", "Temp" & "Humidity" columns to it
    #while tbl_list contains every column, newlist only contains the "Time (CST)", "Temp." and "Humidity" columns
    for i in tbl_list:
        if (i[0] == r"Time (CST)" or i[0] == r"Temp." or i[0] == r"Humidity"):
            newlist.append(i)

    #add the corresponding date to every time entry
    newlist[0] = ["2017/" + str(mth) + "/" + str(dy) + " " + time if time != "Time (CST)" else time for time in newlist[0]]
    #and then increment the date counter
    if (mth==6 or mth==9 or mth==11):
        if (dy>=30):
            mth += 1
            dy = 1
        else:
            dy += 1
    else:
        if (dy>=31):
            mth += 1
            dy = 1
        else:
            dy += 1

    newlist = transpose(newlist) #transpose it back
    df=df.append(pd.DataFrame(newlist)) #append the table for this url page to the overall dataframe
    print(str(j) + "/" + str(len(urls))) #progress counter
    j += 1
#for loop ends here

#setting the header and column index
df.columns = df.iloc[0] #set the first row as the header row (which determines the column names)
df = df.drop_duplicates(subset="Time (CST)", keep=False) #delete all the useless duplicate header rows ('Time', 'Temp' & 'Humidity')in the table data
df = df.set_index("Time (CST)") #set the first column as index

#getting the hourly average
df.index=pd.DatetimeIndex(df.index) #convert date index datatype to DateTime
df.index=df.index.map(lambda x:x.replace(minute=0)) #normalize all time to hours, e.g 6.30PM becomes 6.00PM
                                                    #this will introduce duplicates datetime entries
df['Temp.'] = df['Temp.'].apply(pd.to_numeric, errors='ignore') #I can use to_numeric to convert a column of strings to numbers,
df['Humidity'] = df['Humidity'].apply(lambda x: int(x)) #Or I can use a simple lamba function to do the same
df = df.groupby('Time (CST)').mean() #aggregate the duplicate entries by taking their mean
df['Humidity'] = df['Humidity'].apply(lambda x: int(x)) #mean() converts humidity column data to floats, so convert them back to int

all_days = pd.date_range(df.index.min(), df.index.max(), freq='H')
df = df.reindex(all_days).interpolate()

df.columns = ["Temp/°C", "Humidity/%"] #Add units to column headers
df.to_csv('./Weather Data (May-Nov)(Hourly).csv')
print('The file "Weather Data (May-Nov)(Hourly).csv" has been created in the current folder.')
