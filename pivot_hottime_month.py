import pandas as pd

filename1_f='2018/pivot_living_people_2018'
filename2_f='2017/pivot_living_people_2017'

for idx in range(1,13,1):

    filename1=filename1_f+'{0:02d}.csv'.format(idx)

    df01=pd.read_csv(filename1,encoding='cp949')
    
    # print(df01)
    # print(df01.columns)
    
    df_per_time=pd.pivot_table(data=df01, values='Total_Living_people', index=['YYYYMM','si','gu','dong'], columns='H',aggfunc='mean')
    '''
    시간별 평균
    '''
    # filename2='ttest.csv' 
    # df_per_time.to_csv(filename2,encoding='cp949')
    # print(filename2+'저장완료')
    '''
    13~15
    '''
    df_per_hot=df_per_time.iloc[:,13:16]
    df_per_hot['hot_mean']=round((df_per_hot.loc[:,13]+df_per_hot.loc[:,14]+df_per_hot.loc[:,15])/3,0)
    # df_per_hot['month']=
    mon=str(df_per_hot.index[0][0])
    df_per_hot['month']=mon[4:6]
    # print(df_per_hot)
    df_hottime_month=pd.pivot_table(data=df_per_hot, values='hot_mean',index=['si','gu','dong','month'],aggfunc='mean')
    # print(df_hottime_month)
   
    filename_pivot_f='pivot_hottime_month_2018'
 
    filename_pivot=filename_pivot_f+'{0:02d}.csv'.format(idx)
    df_hottime_month.to_csv(filename_pivot,encoding='cp949')
    print(filename_pivot+'저장완료')
      
      
      
    filename2=filename2_f+'{0:02d}.csv'.format(idx)
  
    df02=pd.read_csv(filename2,encoding='cp949')
      
    # print(df01)
    # print(df01.columns)
      
    df_per_time=pd.pivot_table(data=df02, values='Total_Living_people', index=['YYYYMM','si','gu','dong'], columns='H',aggfunc='mean')
    '''
    시간별 평균
    '''
    # filename2='ttest.csv' 
    # df_per_time.to_csv(filename2,encoding='cp949')
    # print(filename2+'저장완료')
    '''
    13~15
    '''
    df_per_hot=df_per_time.iloc[:,13:16]
    df_per_hot['hot_mean']=round((df_per_hot.loc[:,13]+df_per_hot.loc[:,14]+df_per_hot.loc[:,15])/3,0)
    # df_per_hot['month']=
    mon=str(df_per_hot.index[0][0])
    df_per_hot['month']=mon[4:6]
    # print(df_per_hot)
    df_hottime_month=pd.pivot_table(data=df_per_hot, values='hot_mean',index=['si','gu','dong','month'],aggfunc='mean')
    # print(df_hottime_month)
     
    filename_pivot_f='pivot_hottime_month_2017'
  
    filename_pivot=filename_pivot_f+'{0:02d}.csv'.format(idx)
    df_hottime_month.to_csv(filename_pivot,encoding='cp949')
    print(filename_pivot+'저장완료')