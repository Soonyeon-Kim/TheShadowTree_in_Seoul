import pandas as pd

filename='crossroad_kor.xlsx'
cross=pd.read_excel(filename,index_col=0)

cross_sort=cross.sort_values(by=['sido','gu','dong'])

cross_pivot=pd.pivot_table(cross_sort,index=['sido','gu','dong'],aggfunc='count')

print(cross_pivot)
print(type(cross_pivot))

filename='cross_Analysis_dong.csv'
cross_pivot.to_csv(filename,encoding='EUC-KR')
print(filename+'저장완료')