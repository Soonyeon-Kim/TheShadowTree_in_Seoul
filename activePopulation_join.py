import pandas as pd

filename1_f='2017/LOCAL_PEOPLE_DONG_2017'
filename2_f='2017/LONG_FOREIGNER_DONG_2017'
filename3_f='2017/TEMP_FOREIGNER_DONG_2017'

for idx in range(1,13,1):

    filename1=filename1_f+'{0:02d}.csv'.format(idx)
    filename2=filename2_f+'{0:02d}.csv'.format(idx)
    filename3=filename3_f+'{0:02d}.csv'.format(idx)
    
    df_local=pd.read_csv(filename1)
    
    df_local=df_local.reset_index()
    df_local=df_local.iloc[:,0:4]

    recolumn={df_local.columns[0]:'YYYYMM',df_local.columns[1]:'H',df_local.columns[2]:'Code_Dong',df_local.columns[3]:'Total_Living_people'} 
 
    df_local.rename(columns=recolumn,inplace=True)
    
    
    # print(df_local)
    # print(df_local.columns)
    
    df_long_forei=pd.read_csv(filename2)
    df_long_forei=df_long_forei.reset_index()
    df_long_forei=df_long_forei.iloc[:,0:4]
    
    recolumn2={df_long_forei.columns[0]:'YYYYMM',df_long_forei.columns[1]:'H',df_long_forei.columns[2]:'Code_Dong',df_long_forei.columns[3]:'Total_Living_people'}      
    df_long_forei.rename(columns=recolumn2,inplace=True)
     
    # print(df_long_forei)
    # print(df_long_forei.columns)
     
    df_temp_forei=pd.read_csv(filename3)
    df_temp_forei=df_temp_forei.reset_index()
    df_temp_forei=df_temp_forei.iloc[:,0:4]

    recolumn3={df_temp_forei.columns[0]:'YYYYMM',df_temp_forei.columns[1]:'H',df_temp_forei.columns[2]:'Code_Dong',df_temp_forei.columns[3]:'Total_Living_people'}      
    df_temp_forei.rename(columns=recolumn3,inplace=True)
     
#     print(df_temp_forei)
#     print(df_temp_forei.columns)
    
    df_all_living=pd.concat([df_local,df_long_forei,df_temp_forei],axis=0)
    df_all_living.sort_values(by=['Code_Dong','YYYYMM','H','Total_Living_people'],inplace=True)
#     print(df_all_living)

    filename_month_f='all_living_people_2017'

    filename_month=filename_month_f+'{0:02d}.csv'.format(idx)
    df_all_living.to_csv(filename_month,encoding='cp949')
    print(filename_month+'저장완료')

print('fin')