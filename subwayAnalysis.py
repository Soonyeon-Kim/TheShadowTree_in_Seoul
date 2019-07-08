import pandas as pd

filename='subway_all_merge.xlsx'
subway=pd.read_excel(filename,index_col=0)

subway_sort=subway.sort_values(by=['sido','gu','dong'])

subway_pivot=pd.pivot_table(subway_sort,index=['sido','gu','dong'],values='name',aggfunc='count')

print(subway_pivot)
print(type(subway_pivot))

filename='subway_Analysis_dong.csv'
subway_pivot.to_csv(filename,encoding='EUC-KR')
print(filename+'저장완료')

# filename='subway_all_check.csv'
# cross.to_csv(filename,encoding='EUC-KR')
# print(filename+'저장완료')