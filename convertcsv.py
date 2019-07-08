import pandas as pd

# wfile = open("seoul_cross_2019.csv", mode='r', encoding='utf-8')   
# print(wfile)
filename1='busstop_all_merge.xlsx'
df01=pd.read_excel(filename1,index_col=0)

# 
# # for line in wfile:
# #     print(line)
# #     df01=pd.DataFrame(data=line)
# #     print(df01)
filename2='busstop_all_merge.csv' 
df01.to_csv(filename2,encoding='cp949')
print(filename2+'저장완료')