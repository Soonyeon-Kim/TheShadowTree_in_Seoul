import pandas as pd
from sklearn.preprocessing import scale
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA


filename='kmeans_testing.xlsx'

factor3=pd.read_excel(filename,index_col=0)

# print(factor3.head())

# print(type(factor3))

# factor3 데이터에 대한 군집화 수행 결과가 kmeans 객체 변수로 반환
kmeans=KMeans(n_clusters=4, init='k-means++', max_iter=300, random_state=0).fit(factor3)

# kmeans의 labels_ 속성값을 확인하면 데이터가 어떤 중심에 속하는지 알 수 있음
print(kmeans.labels_)

factor3['cluster']=kmeans.labels_

############################################

pca=PCA(n_components=2)
pca_transformed=pca.fit_transform(factor3)

factor3['pca_x']=pca_transformed[:,0]
factor3['pca_y']=pca_transformed[:,1]

print(factor3.head())

# 각 클러스터의 인덱스 불러오기
marker0_ind=factor3[factor3['cluster']==0].index
print(marker0_ind)
marker1_ind=factor3[factor3['cluster']==1].index
print(marker1_ind)
marker2_ind=factor3[factor3['cluster']==2].index
print(marker2_ind)
marker3_ind=factor3[factor3['cluster']==3].index
print(marker3_ind)
# marker4_ind=factor3[factor3['cluster']==4].index
# print(marker4_ind)
# 군집 값 0,1,2에 해당하는 인덱스로 각 군집 레벨의 좌표값 추출
plt.scatter(x=factor3.loc[marker0_ind,'pca_x'], y=factor3.loc[marker0_ind,'pca_y'],marker='o') #8 2
plt.scatter(x=factor3.loc[marker1_ind,'pca_x'], y=factor3.loc[marker1_ind,'pca_y'],marker='s') #14 5
plt.scatter(x=factor3.loc[marker2_ind,'pca_x'], y=factor3.loc[marker2_ind,'pca_y'],marker='^') #3 13
plt.scatter(x=factor3.loc[marker3_ind,'pca_x'], y=factor3.loc[marker3_ind,'pca_y'],marker='*') #3 4    9개
# plt.scatter(x=factor3.loc[marker4_ind,'pca_x'], y=factor3.loc[marker4_ind,'pca_y'],marker='4') #3 1  10개
plt.xlabel('PCA1')
plt.ylabel('PCA2')

plt.title('3 Clusters Visualization by 2 PCA Components')
plt.show()

from sklearn.metrics import silhouette_samples,silhouette_score

# 모든 개별 데이터의 실루엣 계수 구함
score_samples=silhouette_samples(factor3,factor3['cluster'])
print('silhouette_samples() return of shape',score_samples.shape)

factor3['silhouette_coeff']=score_samples

# 모든 데이터의 평균 실루엣 계수 값 구함
average_score=silhouette_score(factor3,factor3['cluster'])
print('factor3 data set Silhouette Analysis Score:{0:3f}'.format(average_score))

print(factor3)

filename2='k_means_ana.csv'
factor3.to_csv(filename2,encoding='cp949')
print('fin')