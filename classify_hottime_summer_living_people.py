import pandas as pd
import numpy as np
filename_f_2018='2018/pivot_living_people_2018'
filename_f_2017='2017/pivot_living_people_2017'

'''
['YYYYMM', 'H', 'si', 'gu', 'dong', 'Total_Living_people']
'''

concat_list=[]
concat_list2=[]
for idx in range(6,9,1):
    filename_2018=filename_f_2018+'{0:02d}.csv'.format(idx)
    filename_2017=filename_f_2017+'{0:02d}.csv'.format(idx)
    
    df_2018=pd.read_csv(filename_2018,encoding='cp949')
    df_2017=pd.read_csv(filename_2017,encoding='cp949')    
    
    concat_list.append(df_2018)
    concat_list2.append(df_2017)
    
imsi=pd.concat(objs=concat_list, axis=0)
imsi2=pd.concat(concat_list2,axis=0)

file_title='2018/imsi.csv'
# imsi.to_csv(file_title,encoding='cp949')
# print(file_title+'저장완료')

file_title2='2017/imsi2.csv'
# imsi2.to_csv(file_title2,encoding='cp949')
# print(file_title2+'저장완료')

hot_afternoon_2018=pd.read_csv(file_title,index_col=0,encoding='cp949')
# print(hot_afternoon_2018.head())
# print(hot_afternoon_2018.columns)

hot_afternoon_2018=hot_afternoon_2018[hot_afternoon_2018['YYYYMM']>=20180620]
# print(type(hot_afternoon_2018))
hot_afternoon_2018=hot_afternoon_2018[np.logical_and(hot_afternoon_2018['H']>=13,hot_afternoon_2018['H']<=15)]

# print(hot_afternoon_2018)

month_ex=hot_afternoon_2018['YYYYMM'].values[:]
  
month_ex=month_ex.astype(dtype='str')
  
month_list=[]
for idx in month_ex:
    flag=0
    month_list.append(idx[4:6])
  
hot_afternoon_2018['month']=month_list

file_title3='2018/imsi3.csv'
hot_afternoon_2018.to_csv(file_title3,encoding='cp949')
print(file_title3+'저장완료')

hot_afternoon_2018_pivot_hour=pd.pivot_table(data=hot_afternoon_2018, values='Total_Living_people', index=['si','gu','dong'], columns='H', aggfunc='mean')
hot_afternoon_2018_pivot_hour['Average']=round((hot_afternoon_2018_pivot_hour.iloc[:,0]+hot_afternoon_2018_pivot_hour.iloc[:,1]+hot_afternoon_2018_pivot_hour.iloc[:,2])/3,0)
print(hot_afternoon_2018_pivot_hour) # 시간별 생활인구 수 
  
 
hot_afternoon_2018_pivot_month=pd.pivot_table(hot_afternoon_2018,values='Total_Living_people', index=['si','gu','dong'], columns='month', aggfunc='mean')
hot_afternoon_2018_pivot_month['Average']=round((hot_afternoon_2018_pivot_month.iloc[:,0]*33+hot_afternoon_2018_pivot_month.iloc[:,1]*93+hot_afternoon_2018_pivot_month.iloc[:,2]*93)/219,0)
    
print(hot_afternoon_2018_pivot_month)
    
filename_pivot_f='pivot_hottime_month_2018_edit.csv'
hot_afternoon_2018_pivot_month.to_csv(filename_pivot_f,encoding='cp949')
print(filename_pivot_f+'저장완료')
     
filename_pivot_f2='pivot_hottime_houly_2018_edit.csv'
hot_afternoon_2018_pivot_hour.to_csv(filename_pivot_f2,encoding='cp949')
print(filename_pivot_f2+'저장완료')
    
###################