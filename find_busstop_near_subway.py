import pandas as pd
import math
from pandas import DataFrame

filename1='busstop_all_merge.xlsx'
df1=pd.read_excel(filename1,index_col=0)
# print(df1.columns)
# print(df1.head())
df1=df1.drop(['latitude_y','name','longitude_y'],axis=1)
print(df1.head())

filename2='subway_all_merge.xlsx'
df2=pd.read_excel(filename2,index_col=0)
# print(df2.columns)
# print(df2.head())

df2=df2.drop(['name', 'line', 'line_detail', 'address', 'latitude_x','longitude_x'],axis=1)
print(df2.head())

 
buslist=[]
for idx in range(len(df1['latitude_x'])): #11018
    lati_bus=df1['latitude_x'][idx]
    longi_bus=df1['longitude_x'][idx]
    buslist.append([lati_bus,longi_bus]) # 버스 좌표
 
# print(buslist)

sublist=[]
for idx in range(len(df2['latitude_y'])): #387
    lati_sub=df2['latitude_y'][idx]
    longi_sub=df2['longitude_y'][idx]
    sublist.append([lati_sub,longi_sub]) # 지하철 좌표
 
# print(sublist)

nearsubway=[]
testa=[]
for idx3 in range(len(sublist)):
    subway_lat=sublist[idx3][0]
    subway_long=sublist[idx3][1]

    for idx2 in range(len(buslist)):
        bus_lat=buslist[idx2][0]
        bus_long=buslist[idx2][1]

        dist_lat=subway_lat-bus_lat
        dist_long=subway_long-bus_long
        target100=math.sqrt(((111*dist_lat)**2)+((88*dist_long)**2))
 
        if target100<=0.1:
#             print((subway_lat,subway_long,bus_lat,bus_long))
            nearsubway.append((subway_lat,subway_long,bus_lat,bus_long))

  
nearcolumn=['subway_lat','subway_long','bus_lat','bus_long']

myframe=DataFrame(nearsubway,columns=nearcolumn)

myframe=myframe.drop_duplicates(nearcolumn, keep='first')

filename='busstop_near_subway.xlsx'

myframe.to_excel(filename,encoding='EUC-KR')
print(filename+'저장완료')