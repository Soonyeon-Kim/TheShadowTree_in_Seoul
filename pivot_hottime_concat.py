import pandas as pd

filename1_f='2018/pivot_hottime_month_2018'
filename2_f='2017/pivot_hottime_month_2017'

all_data_list_2018=[]
all_data_list_2017=[]

for idx in range(1,13,1):

    filename1=filename1_f+'{0:02d}.csv'.format(idx)
    filename2=filename2_f+'{0:02d}.csv'.format(idx)

    df01=pd.read_csv(filename1,encoding='cp949')
    df02=pd.read_csv(filename2,encoding='cp949')
    
    all_data_list_2018.append(df01)
    all_data_list_2017.append(df02)
    
df_hot_2018=pd.concat(all_data_list_2018,axis=0)
df_hot_2017=pd.concat(all_data_list_2017,axis=0)

filename_2018_f='yearly_hottime_2018.csv'
filename_2017_f='yearly_hottime_2017.csv'

df_hot_2018.to_csv(filename_2018_f,encoding='cp949')
print(filename_2018_f+'저장완료')
df_hot_2017.to_csv(filename_2017_f,encoding='cp949')
print(filename_2017_f+'저장완료')
print('fin')

filename='yearly_hottime_2018.csv'

df_mean=pd.read_csv(filename,encoding='cp949',index_col=0)
# print(df_mean)

df_mean_pivot_yearly=pd.pivot_table(data=df_mean, values='hot_mean', index=['si','gu','dong'], aggfunc='mean')
# print(df_mean_pivot_yearly) # 연 평균, 동별
filename_yearly='living_people_yearly_dong_2018.csv'
df_mean_pivot_yearly.to_csv(filename_yearly,encoding='cp949')
print(filename_yearly+'저장완료')

df_mean_pivot_monthly=pd.pivot_table(data=df_mean, values='hot_mean', index=['si','gu','dong'],columns='month', aggfunc='mean')
print(df_mean_pivot_monthly) # 월 평균, 동별
filename_monthly='living_people_monthly_dong_2018.csv'
df_mean_pivot_monthly.to_csv(filename_monthly,encoding='cp949')
print(filename_monthly+'저장완료')

##############################################
filename_2017='yearly_hottime_2017.csv'

df_mean_2017=pd.read_csv(filename_2017,encoding='cp949',index_col=0)
# print(df_mean)

df_mean_pivot_2017=pd.pivot_table(data=df_mean_2017, values='hot_mean', index=['si','gu','dong'], aggfunc='mean')
# print(df_mean_pivot_yearly) # 연 평균, 동별
filename_2017='living_people_yearly_dong_2017.csv'
df_mean_pivot_2017.to_csv(filename_2017,encoding='cp949')
print(filename_2017+'저장완료')

df_mean_pivot_2017_monthly=pd.pivot_table(data=df_mean_2017, values='hot_mean', index=['si','gu','dong'],columns='month', aggfunc='mean')
print(df_mean_pivot_2017_monthly) # 월 평균, 동별
filename_2017_monthly='living_people_monthly_dong_2017.csv'
df_mean_pivot_2017_monthly.to_csv(filename_2017_monthly,encoding='cp949')
print(filename_2017_monthly+'저장완료')