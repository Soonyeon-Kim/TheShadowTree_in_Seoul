import pandas as pd
filename1_f='2018/all_living_people_2018'
filename2_f='2017/all_living_people_2017'

for idx in range(1,13,1):

    filename1=filename1_f+'{0:02d}.csv'.format(idx)
    
    living_people=pd.read_csv(filename1)
    
    living_people=living_people.iloc[:,1:5]
    
    filename_code='code_mapping_2018.xlsx'
    
    mapping=pd.read_excel(filename_code)
    # print(mapping)
    
    living_mapping=living_people.merge(mapping,left_on='Code_Dong',right_on='code')
    living_mapping.drop(columns=['code','Code_Dong'],inplace=True)
    # print(living_mapping.columns)

    living_pivot=pd.pivot_table(living_mapping, values='Total_Living_people', index=['YYYYMM','H','si','gu','dong'],aggfunc='sum')
      
#     print(living_pivot)
    
    filename_pivot_f='pivot_living_people_2018'

    filename_pivot=filename_pivot_f+'{0:02d}.csv'.format(idx)
    living_pivot.to_csv(filename_pivot,encoding='cp949')
    print(filename_pivot+'저장완료')


    
    filename2=filename2_f+'{0:02d}.csv'.format(idx)
    
    living_people2=pd.read_csv(filename2)
    
    living_people2=living_people2.iloc[:,1:5]
    
    living_mapping2=living_people2.merge(mapping,left_on='Code_Dong',right_on='code')
    living_mapping2.drop(columns=['code','Code_Dong'],inplace=True)
    # print(living_mapping2.columns)
    
    
    
    living_pivot2=pd.pivot_table(living_mapping2, values='Total_Living_people', index=['YYYYMM','H','si','gu','dong'],aggfunc='sum')
      
#     print(living_pivot)
    
    filename_pivot_f2='pivot_living_people_2017'

    filename_pivot2=filename_pivot_f2+'{0:02d}.csv'.format(idx)
    living_pivot2.to_csv(filename_pivot2,encoding='cp949')
    print(filename_pivot2+'저장완료')