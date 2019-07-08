import pandas as pd

filename1='sub_all_seoul.xlsx'
df1=pd.read_excel(filename1)

# dataframe
# print(df1)
# print(type(df1))

filename2='subway_all_2018.xlsx'
df2=pd.read_excel(filename2,index_col=0)

# print(df2)
# print(type(df2))

df_merged = df1.merge(df2, how='outer', left_index=True, right_index=True)

print(df_merged)

filename3='subway_all_merge.xlsx'
df_merged.to_excel(filename3,encoding='EUC-KR')
print(filename3+'저장완료')