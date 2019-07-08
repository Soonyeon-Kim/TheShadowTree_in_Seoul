import pandas as pd
from pyproj import Proj, transform  #Should install pyproj module.

filename = 'TL_TBVIATR_FCLTY_INFO_2017.csv'
jibgak=pd.read_csv(filename,encoding='cp949')

# print(jibgak)

jibgak=jibgak.iloc[:,1:15]

jibgak=jibgak.drop(['VIAT_SE_CD','VIAT_CD','ADRES_CD','ADRES_NM','TELNO'],axis=1)

# print(jibgak)
# print(jibgak.columns)

# Change coordinate system
# korea 2000/central belt 2010 (epsg:5186) to wgs84(epsg:4326)
inProj = Proj(init = 'epsg:5181')
outProj= Proj(init = 'epsg:4326')
latitude = []
longitude= []
for idx,row in jibgak.iterrows():

    
    x,y  = row.X_VALUE,row.Y_VALUE  # korea 2000 좌표계
    nx,ny = transform(inProj,outProj,x,y)     # 새로운 좌표계    
    latitude.append(ny)
    longitude.append(nx)
#     print(idx)
jibgak['latitude'] = latitude
jibgak['longitude']= longitude
 
filename1='jibhak_long_lat.csv'
jibgak.to_csv(filename1,encoding='cp949')
print('fin')