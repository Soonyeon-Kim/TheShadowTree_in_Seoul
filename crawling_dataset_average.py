import pandas as pd
from pandas import DataFrame
from numpy import nan


df = pd.read_csv('온도크롤링.csv', encoding='cp949')
#현충원을 동작구로 대체, 서울을 종로로 대체(주소지)
df = df.rename(columns = {'현충원': '동작'})
df = df.rename(columns = {'서울': '종로'})
df = df.replace('.',nan)

for item in df.columns:
    
    if df[item].dtype == 'object':  
        df[item] = df[item].astype('float')
        
    if item not in ('종로','중구','용산','성동','광진','동대문','중랑','성북', \
                    '강북', '도봉','노원','은평','서대문','마포','양천','강서','구로', \
                    '금천','영등포','동작','관악','서초','강남','송파','강동'):
        
        del df[item]
    else:
        if item[-1] != '구':
            df = df.rename(columns = {item: item+'구'})
 
#결측치 처리
#df.info() 필수
mean_data = round(df.mean(),1)

df = df.fillna(mean_data)

mean_df = DataFrame(round(df.mean(axis=0),1),columns=['평균'])

mean_df.to_csv('평균.csv', mode='w', encoding='cp949')
print('finished')