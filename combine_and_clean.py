
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import glob
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#importing weather data
weather=pd.read_csv("./Weather Data.csv")
weather["ts"]=pd.to_datetime(weather["ts"], format="%d/%m/%y %H:%M")
weather["ts"]=weather["ts"].dt.strftime("%Y-%m-%d %H:%M:%S")
weather=weather.set_index("ts")
weather.index=pd.DatetimeIndex(weather.index)
#creating a new index
all_days = pd.date_range(weather.index.min(), weather.index.max(), freq='H')
#weather=weather.reindex(all_days)
#imputing missing values in weather data
#weather=weather.interpolate(method="linear",axis=0)


# In[3]:


#importing data files for all the months separately
#POWER
df_p_c1 = [pd.read_csv(file,index_col="ts") for file in glob.glob('./Raw Data/Chiller1_power/*.csv')]
df_p_c2 = [pd.read_csv(file,index_col="ts") for file in glob.glob('./Raw Data/Chiller2_power/*.csv')]
df_p_c3 = [pd.read_csv(file,index_col="ts") for file in glob.glob('./Raw Data/Chiller3_power/*.csv')]
df_p_c4 = [pd.read_csv(file,index_col="ts") for file in glob.glob('./Raw Data/Chiller4_power/*.csv')]

#TEMP
df_t_c1 = [pd.read_csv(file,index_col="ts") for file in glob.glob('./Raw Data/Chiller1_temp/*.csv')]
df_t_c2 = [pd.read_csv(file,index_col="ts") for file in glob.glob('./Raw Data/Chiller2_temp/*.csv')]
df_t_c3 = [pd.read_csv(file,index_col="ts") for file in glob.glob('./Raw Data/Chiller3_temp/*.csv')]
df_t_c4 = [pd.read_csv(file,index_col="ts") for file in glob.glob('./Raw Data/Chiller4_temp/*.csv')]

#EVAPORATOR
df_e_c1 = [pd.read_csv(file,index_col="ts") for file in glob.glob('./Raw Data/Chiller1_evaflow/*.csv')]
df_e_c2 = [pd.read_csv(file,index_col="ts") for file in glob.glob('./Raw Data/Chiller2_evaflow/*.csv')]
df_e_c3 = [pd.read_csv(file,index_col="ts") for file in glob.glob('./Raw Data/Chiller3_evaflow/*.csv')]
df_e_c4 = [pd.read_csv(file,index_col="ts") for file in glob.glob('./Raw Data/Chiller4_evaflow/*.csv')]

#CONDENSER
df_c_c1 = [pd.read_csv(file,index_col="ts") for file in glob.glob('./Raw Data/Chiller1_conflow/*.csv')]
df_c_c2 = [pd.read_csv(file,index_col="ts") for file in glob.glob('./Raw Data/Chiller2_conflow/*.csv')]
df_c_c3 = [pd.read_csv(file,index_col="ts") for file in glob.glob('./Raw Data/Chiller3_conflow/*.csv')]
df_c_c4 = [pd.read_csv(file,index_col="ts") for file in glob.glob('./Raw Data/Chiller4_conflow/*.csv')]


# In[4]:


#concatenating the dataframes and subsetting the columns
#POWER
tab_p_c1=pd.concat(df_p_c1).sort_index()
tab_p_c2=pd.concat(df_p_c2).sort_index()
tab_p_c3=pd.concat(df_p_c3).sort_index()
tab_p_c4=pd.concat(df_p_c4).sort_index()

tab_p_c1=tab_p_c1[["ch1Watt","ch2Watt","ch3Watt","totalPositiveWattHour"]]
tab_p_c2=tab_p_c2[["ch1Watt","ch2Watt","ch3Watt","totalPositiveWattHour"]]
tab_p_c3=tab_p_c3[["ch1Watt","ch2Watt","ch3Watt","totalPositiveWattHour"]]
tab_p_c4=tab_p_c4[["ch1Watt","ch2Watt","ch3Watt","totalPositiveWattHour"]]

tab_p_c1.columns=["C1ch1Watt","C1ch2Watt","C1ch3Watt","C1totalPositiveWattHour"]
tab_p_c2.columns=["C2ch1Watt","C2ch2Watt","C2ch3Watt","C2totalPositiveWattHour"]
tab_p_c3.columns=["C3ch1Watt","C3ch2Watt","C3ch3Watt","C3totalPositiveWattHour"]
tab_p_c4.columns=["C4ch1Watt","C4ch2Watt","C4ch3Watt","C4totalPositiveWattHour"]

#TEMP
tab_t_c1=pd.concat(df_t_c1).sort_index()
tab_t_c2=pd.concat(df_t_c2).sort_index()
tab_t_c3=pd.concat(df_t_c3).sort_index()
tab_t_c4=pd.concat(df_t_c4).sort_index()

tab_t_c1=tab_t_c1[["value1","value2","value3","value4"]]
tab_t_c2=tab_t_c2[["value1","value2","value3","value4"]]
tab_t_c3=tab_t_c3[["value1","value2","value3","value4"]]
tab_t_c4=tab_t_c4[["value1","value2","value3","value4"]]

tab_t_c1.columns=["C1temp1","C1temp2","C1temp3","C1temp4"]
tab_t_c2.columns=["C2temp1","C2temp2","C2temp3","C2temp4"]
tab_t_c3.columns=["C3temp1","C3temp2","C3temp3","C3temp4"]
tab_t_c4.columns=["C4temp1","C4temp2","C4temp3","C4temp4"]

#EVAPORATOR
tab_e_c1=pd.concat(df_e_c1).sort_index()
tab_e_c2=pd.concat(df_e_c2).sort_index()
tab_e_c3=pd.concat(df_e_c3).sort_index()
tab_e_c4=pd.concat(df_e_c4).sort_index()

tab_e_c1=tab_e_c1[["flowRate","flowSpeed","totalFlowRate"]]
tab_e_c2=tab_e_c2[["flowRate","flowSpeed","totalFlowRate"]]
tab_e_c3=tab_e_c3[["flowRate","flowSpeed","totalFlowRate"]]
tab_e_c4=tab_e_c4[["flowRate","flowSpeed","totalFlowRate"]]

tab_e_c1.columns=["C1e.flowRate","C1e.flowSpeed","C1e.totalFlowRate"]
tab_e_c2.columns=["C2e.flowRate","C2e.flowSpeed","C2e.totalFlowRate"]
tab_e_c3.columns=["C3e.flowRate","C3e.flowSpeed","C3e.totalFlowRate"]
tab_e_c4.columns=["C4e.flowRate","C4e.flowSpeed","C4e.totalFlowRate"]

#CONDENSER
tab_c_c1=pd.concat(df_c_c1).sort_index()
tab_c_c2=pd.concat(df_c_c2).sort_index()
tab_c_c3=pd.concat(df_c_c3).sort_index()
tab_c_c4=pd.concat(df_c_c4).sort_index()

tab_c_c1=tab_c_c1[["flowRate","flowSpeed","totalFlowRate"]]
tab_c_c2=tab_c_c2[["flowRate","flowSpeed","totalFlowRate"]]
tab_c_c3=tab_c_c3[["flowRate","flowSpeed","totalFlowRate"]]
tab_c_c4=tab_c_c4[["flowRate","flowSpeed","totalFlowRate"]]

tab_c_c1.columns=["C1c.flowRate","C1c.flowSpeed","C1c.totalFlowRate"]
tab_c_c2.columns=["C2c.flowRate","C2c.flowSpeed","C2c.totalFlowRate"]
tab_c_c3.columns=["C3c.flowRate","C3c.flowSpeed","C3c.totalFlowRate"]
tab_c_c4.columns=["C4c.flowRate","C4c.flowSpeed","C4c.totalFlowRate"]


# ## Drop outliers

# In[5]:


#TEMP
#keep rows with temp value less than 60 and not 0

tab_t_c1 = tab_t_c1[(tab_t_c1.C1temp1!=0) & (tab_t_c1.C1temp2!=0) & (tab_t_c1.C1temp3!=0) & (tab_t_c1.C1temp4!=0)]
tab_t_c1 = tab_t_c1[(tab_t_c1.C1temp1<60) & (tab_t_c1.C1temp2<60) & (tab_t_c1.C1temp3<60) & (tab_t_c1.C1temp4<60)]

tab_t_c2 = tab_t_c2[(tab_t_c2.C2temp1!=0) & (tab_t_c2.C2temp2!=0) & (tab_t_c2.C2temp3!=0) & (tab_t_c2.C2temp4!=0)]
tab_t_c2 = tab_t_c2[(tab_t_c2.C2temp1<60) & (tab_t_c2.C2temp2<60) & (tab_t_c2.C2temp3<60) & (tab_t_c2.C2temp4<60)]

tab_t_c3 = tab_t_c3[(tab_t_c3.C3temp1!=0) & (tab_t_c3.C3temp2!=0) & (tab_t_c3.C3temp3!=0) & (tab_t_c3.C3temp4!=0)]
tab_t_c3 = tab_t_c3[(tab_t_c3.C3temp1<60) & (tab_t_c3.C3temp2<60) & (tab_t_c3.C3temp3<60) & (tab_t_c3.C3temp4<60)]

tab_t_c4 = tab_t_c4[(tab_t_c4.C4temp1!=0) & (tab_t_c4.C4temp2!=0) & (tab_t_c4.C4temp3!=0) & (tab_t_c4.C4temp4!=0)]
tab_t_c4 = tab_t_c4[(tab_t_c4.C4temp1<60) & (tab_t_c4.C4temp2<60) & (tab_t_c4.C4temp3<60) & (tab_t_c4.C4temp4<60)]


# In[6]:


#EVAPORATOR
#chiller 1 accumulated flow rate should be higher than start point
tab_e_c1 = tab_e_c1[tab_e_c1['C1e.totalFlowRate']>=tab_e_c1['C1e.totalFlowRate'].iloc[0]]

#chiller 2 one outlier
tab_e_c2 = tab_e_c2[tab_e_c2['C2e.totalFlowRate']<1000000]

#chiller 3 has 4 times accumulated flow rate overshoots max meter range
tab_e_c3.loc[tab_e_c3.index>='2017-06-28 15:23:07.843','C3e.totalFlowRate']+=100000000
tab_e_c3.loc[tab_e_c3.index>='2017-08-15 06:43:34.668','C3e.totalFlowRate']+=100000000
tab_e_c3.loc[tab_e_c3.index>='2017-09-23 22:22:19.768','C3e.totalFlowRate']+=100000000
tab_e_c3.loc[tab_e_c3.index>='2017-11-23 05:48:00.432','C3e.totalFlowRate']+=100000000

#chiller 4 is normal
#However, chiller 4 eva flow Oct data is duplicate of Nov, need wait for Rubio to update.


# In[7]:


#CONDENSER
#chiller 1 and 4 have outliers, 2 and 3 are normal
tab_c_c1=tab_c_c1[(tab_c_c1['C1c.totalFlowRate']>0) & (tab_c_c1['C1c.totalFlowRate']>10000)]
tab_c_c4=tab_c_c4[tab_c_c4['C4c.totalFlowRate']>0]


# In[8]:


#creating a list for dataframes
tables=[tab_p_c1,tab_t_c1,tab_e_c1,tab_c_c1,tab_p_c2,tab_t_c2,tab_e_c2,tab_c_c2,
        tab_p_c3,tab_t_c3,tab_e_c3,tab_c_c3,tab_p_c4,tab_t_c4,tab_e_c4,tab_c_c4]


# In[9]:


#changing the index to datetimeindex
for i in tables:
    i.index=pd.DatetimeIndex(i.index)
    i.index=i.index.map(lambda x:x.replace(second=0,microsecond=0))


# In[10]:


#removing duplicates
tab_p_c1=tab_p_c1.reset_index().drop_duplicates(subset="ts",keep="first").set_index("ts")
tab_t_c1=tab_t_c1.reset_index().drop_duplicates(subset="ts",keep="first").set_index("ts")
tab_e_c1=tab_e_c1.reset_index().drop_duplicates(subset="ts",keep="first").set_index("ts")
tab_c_c1=tab_c_c1.reset_index().drop_duplicates(subset="ts",keep="first").set_index("ts")

tab_p_c2=tab_p_c2.reset_index().drop_duplicates(subset="ts",keep="first").set_index("ts")
tab_t_c2=tab_t_c2.reset_index().drop_duplicates(subset="ts",keep="first").set_index("ts")
tab_e_c2=tab_e_c2.reset_index().drop_duplicates(subset="ts",keep="first").set_index("ts")
tab_c_c2=tab_c_c2.reset_index().drop_duplicates(subset="ts",keep="first").set_index("ts")

tab_p_c3=tab_p_c3.reset_index().drop_duplicates(subset="ts",keep="first").set_index("ts")
tab_t_c3=tab_t_c3.reset_index().drop_duplicates(subset="ts",keep="first").set_index("ts")
tab_e_c3=tab_e_c3.reset_index().drop_duplicates(subset="ts",keep="first").set_index("ts")
tab_c_c3=tab_c_c3.reset_index().drop_duplicates(subset="ts",keep="first").set_index("ts")

tab_p_c4=tab_p_c4.reset_index().drop_duplicates(subset="ts",keep="first").set_index("ts")
tab_t_c4=tab_t_c4.reset_index().drop_duplicates(subset="ts",keep="first").set_index("ts")
tab_e_c4=tab_e_c4.reset_index().drop_duplicates(subset="ts",keep="first").set_index("ts")
tab_c_c4=tab_c_c4.reset_index().drop_duplicates(subset="ts",keep="first").set_index("ts")


# ### DOWNSAMPLE DATA TO HOURLY

# In[11]:


tab_p_c1=tab_p_c1.resample("H").mean().reindex(all_days)
tab_t_c1=tab_t_c1.resample("H").mean().reindex(all_days)
tab_e_c1=tab_e_c1.resample("H").mean().reindex(all_days)
tab_c_c1=tab_c_c1.resample("H").mean().reindex(all_days)

tab_p_c2=tab_p_c2.resample("H").mean().reindex(all_days)
tab_t_c2=tab_t_c2.resample("H").mean().reindex(all_days)
tab_e_c2=tab_e_c2.resample("H").mean().reindex(all_days)
tab_c_c2=tab_c_c2.resample("H").mean().reindex(all_days)

tab_p_c3=tab_p_c3.resample("H").mean().reindex(all_days)
tab_t_c3=tab_t_c3.resample("H").mean().reindex(all_days)
tab_e_c3=tab_e_c3.resample("H").mean().reindex(all_days)
tab_c_c3=tab_c_c3.resample("H").mean().reindex(all_days)

tab_p_c4=tab_p_c4.resample("H").mean().reindex(all_days)
tab_t_c4=tab_t_c4.resample("H").mean().reindex(all_days)
tab_e_c4=tab_e_c4.resample("H").mean().reindex(all_days)
tab_c_c4=tab_c_c4.resample("H").mean().reindex(all_days)


# ## Add in parameters

# In[12]:


#Calculate hourly power from accumulated power
tab_p_c1['C1PositiveWattHour']=tab_p_c1['C1totalPositiveWattHour'].diff().shift(-1)
tab_p_c2['C2PositiveWattHour']=tab_p_c2['C2totalPositiveWattHour'].diff().shift(-1)
tab_p_c3['C3PositiveWattHour']=tab_p_c3['C3totalPositiveWattHour'].diff().shift(-1)
tab_p_c4['C4PositiveWattHour']=tab_p_c4['C4totalPositiveWattHour'].diff().shift(-1)

#Calculate temperature difference
tab_t_c1['C1t2-t1'] = tab_t_c1['C1temp2']-tab_t_c1['C1temp1']
tab_t_c2['C2t2-t1'] = tab_t_c2['C2temp2']-tab_t_c2['C2temp1']
tab_t_c3['C3t2-t1'] = tab_t_c3['C3temp2']-tab_t_c3['C3temp1']
tab_t_c4['C4t2-t1'] = tab_t_c4['C4temp2']-tab_t_c4['C4temp1']

tab_t_c1['C1t3-t4'] = tab_t_c1['C1temp3']-tab_t_c1['C1temp4']
tab_t_c2['C2t3-t4'] = tab_t_c2['C2temp3']-tab_t_c2['C2temp4']
tab_t_c3['C3t3-t4'] = tab_t_c3['C3temp3']-tab_t_c3['C3temp4']
tab_t_c4['C4t3-t4'] = tab_t_c4['C4temp3']-tab_t_c4['C4temp4']

#Calculate cooling capacity
cc_c1=pd.DataFrame()
cc_c2=pd.DataFrame()
cc_c3=pd.DataFrame()
cc_c4=pd.DataFrame()
cc_c1['C1Coolingcap']=999.68844162593*tab_e_c1['C1e.flowRate']*0.001/60*4.19*tab_t_c1['C1t2-t1']
cc_c2['C2Coolingcap']=999.68844162593*tab_e_c2['C2e.flowRate']*0.001/60*4.19*tab_t_c2['C2t2-t1']
cc_c3['C3Coolingcap']=999.68844162593*tab_e_c3['C3e.flowRate']*0.001/60*4.19*tab_t_c3['C3t2-t1']
cc_c4['C4Coolingcap']=999.68844162593*tab_e_c4['C4e.flowRate']*0.001/60*4.19*tab_t_c4['C4t2-t1']

#Determining if Chiller is on/off
cc_c1['C1 O/F'] = tab_p_c1['C1PositiveWattHour'] > 0
cc_c2['C2 O/F'] = tab_p_c2['C2PositiveWattHour'] > 0
cc_c3['C3 O/F'] = tab_p_c3['C3PositiveWattHour'] > 0
cc_c4['C4 O/F'] = tab_p_c4['C4PositiveWattHour'] > 0


# ### Merging all the dataframes

# In[13]:


#merging the dataframes
c1_final=tab_p_c1.merge(tab_t_c1,left_index=True, right_index=True).merge(tab_e_c1,left_index=True, right_index=True).merge(tab_c_c1,left_index=True, right_index=True).merge(cc_c1,left_index=True, right_index=True)
c2_final=tab_p_c2.merge(tab_t_c2,left_index=True, right_index=True).merge(tab_e_c2,left_index=True, right_index=True).merge(tab_c_c2,left_index=True, right_index=True).merge(cc_c2,left_index=True, right_index=True)
c3_final=tab_p_c3.merge(tab_t_c3,left_index=True, right_index=True).merge(tab_e_c3,left_index=True, right_index=True).merge(tab_c_c3,left_index=True, right_index=True).merge(cc_c3,left_index=True, right_index=True)
c4_final=tab_p_c4.merge(tab_t_c4,left_index=True, right_index=True).merge(tab_e_c4,left_index=True, right_index=True).merge(tab_c_c4,left_index=True, right_index=True).merge(cc_c4,left_index=True, right_index=True)


# ## Imputing Missing Values

# In[14]:


#merging with weather
final=c1_final.merge(c2_final,left_index=True, right_index=True).merge(c3_final,left_index=True, right_index=True).merge(c4_final,left_index=True, right_index=True).merge(weather,left_index=True,right_index=True)


# In[15]:


final


# In[16]:


corr_matrix = final.corr().abs()
high_corr_var=np.where(corr_matrix>0.8)
high_corr_var=[(corr_matrix.index[x],corr_matrix.columns[y]) for x,y in zip(*high_corr_var) if x!=y and x>y]


# In[17]:


high_corr_var


# In[18]:


final.to_csv('./Total Data.csv')


# ## Evaluation
print('From chiller 1 to 4, the number of rows whereby there is no \nevaporator flow but there are still power consumption are as follow')
print(c1[(c1.C1PositiveWattHour!=0)&(c1["C1e.flowRate"]==0)].count().iloc[0])
print(c2[(c2.C2PositiveWattHour!=0)&(c2["C2e.flowRate"]==0)].count().iloc[0])
print(c3[(c3.C3PositiveWattHour!=0)&(c3["C3e.flowRate"]==0)].count().iloc[0])
print(c4[(c4.C4PositiveWattHour!=0)&(c4["C4e.flowRate"]==0)].count().iloc[0])c1.to_csv('./../formeonly.csv')c1=c1.fillna(0)
c2=c2.fillna(0)
c3=c3.fillna(0)
c4=c4.fillna(0)

c1.index.name='ts'
c2.index.name='ts'
c3.index.name='ts'
c4.index.name='ts'
