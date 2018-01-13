import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import glob
#matplotlib inline

df_p = [pd.read_csv(file,index_col="ts") for file in glob.glob('./Raw Data/Chiller2_power/*.csv')]
df_t = [pd.read_csv(file,index_col="ts") for file in glob.glob('./Raw Data/Chiller2_temp/*.csv')]
df_e = [pd.read_csv(file,index_col="ts") for file in glob.glob('./Raw Data/Chiller2_evaflow/*.csv')]
df_c = [pd.read_csv(file,index_col="ts") for file in glob.glob('./Raw Data/Chiller2_conflow/*.csv')]

tab_p=pd.concat(df_p).sort_index()
tab_p=tab_p[["ch1Watt","ch2Watt","ch3Watt","totalPositiveWattHour"]]
tab_p.columns=["C2ch1Watt","C2ch2Watt","C2ch3Watt","C2totalPositiveWattHour"]

tab_t=pd.concat(df_t).sort_index()
tab_t=tab_t[["value1","value2","value3","value4"]]
tab_t.columns=["C2temp1","C2temp2","C2temp3","C2temp4"]

tab_e=pd.concat(df_e).sort_index()
tab_e=tab_e[["flowRate","flowSpeed","totalFlowRate"]]
tab_e.columns=["C2e.flowRate","C2e.flowSpeed","C2e.totalFlowRate"]

tab_c=pd.concat(df_c).sort_index()
tab_c=tab_c[["flowRate","flowSpeed","totalFlowRate"]]
tab_c.columns=["C2c.flowRate","C2c.flowSpeed","C2c.totalFlowRate"]

# tab_e[tab_e['e.totalFlowRate']<0]

# tab_e.loc['2017-07-25 00:09:03.427','e.totalFlowRate']=217369

# tab_e.loc['2017-09-27 11:05:17.788','e.totalFlowRate']=300511

# tab_e.describe()

# tab_c[tab_c['c.totalFlowRate']<190000]

# tab_c.loc['2017-05-10 14:39:24.901','c.totalFlowRate']=218047

# tab_c.loc['2017-06-18 21:10:17.948','c.totalFlowRate']=239261

# tab_c.describe()

tables=[tab_p,tab_t,tab_e,tab_c]

for i in tables:
    i.index=pd.DatetimeIndex(i.index)
    i.index=i.index.map(lambda x:x.replace(minute=0,second=0,microsecond=0))
print(tab_p.shape,tab_t.shape,tab_e.shape,tab_c.shape)

result_p = tab_p.groupby('ts').mean()
result_p['C2totalPositiveWattHour'] = tab_p['C2totalPositiveWattHour'].groupby('ts').min()-tab_p['C2totalPositiveWattHour'].min()

result_t = tab_t.groupby('ts').mean()

result_e = tab_e.groupby('ts').mean()
result_e['C2e.totalFlowRate'] = tab_e['C2e.totalFlowRate'].groupby('ts').min()-tab_e['C2e.totalFlowRate'].min()

result_c = tab_c.groupby('ts').mean()
result_c['C2c.totalFlowRate'] = tab_c['C2c.totalFlowRate'].groupby('ts').min()-tab_c['C2c.totalFlowRate'].min()

all_days = pd.date_range(result_p.index.min(), result_p.index.max(), freq='H')
# results=[result_p,result_t,result_e,result_c]
# for j in results:
#     j = j.reindex(all_days)
#     j = j.interpolate()
result_p = result_p.reindex(all_days).interpolate()
result_t = result_t.reindex(all_days).interpolate()
result_e = result_e.reindex(all_days).interpolate()
result_c = result_c.reindex(all_days).interpolate()

c1_final=result_p.merge(result_t,left_index=True, right_index=True).merge(result_e,left_index=True, right_index=True).merge(result_c,left_index=True, right_index=True)

c1_final

c1_final.describe()

c1_final.info()
#May-Nov has (31 + 30 + 31 + 31 + 30 + 31 + 30)(24) = 5136 hours in total.  There should be 5136 entries

c1_final.to_csv('Chiller2 Data (May-Nov)(Hourly).csv')
