import pandas as pd

filename1='busstop_near_subway.xlsx'
df1=pd.read_excel(filename1,index_col=0)

filename2='subway_all_merge.xlsx'
df2=pd.read_excel(filename2,index_col=0)

print(df1.head())
print(type(df1))


print(df2.head())
print(type(df2))
print(df2.columns)