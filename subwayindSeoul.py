import ssl, json, datetime, folium, webbrowser
import pandas as pd
import urllib.request
from pandas import DataFrame

print('서울시  지하철 주소 찾기')
filename = 'sub_all_seoul.xlsx' 
# 삼전역부터 임의 추가함
df_raw=pd.read_excel(filename,encoding='utf-8')
print(df_raw.head())

print(len(df_raw['longitude']))

def get_request_url(url):
    client_id = ""
    client_secret = ""
      
    req=urllib.request.Request(url)
    req.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    req.add_header('X-NCP-APIGW-API-KEY', client_secret)
      
    try:
        context=ssl._create_unverified_context()
        response=urllib.request.urlopen(req,context=context)
        if response.getcode()==200:
#             print('[%s] url request success' % datetime.datetime.now())
            return response.read().decode('utf-8')
          
    except Exception as err:
        print(err)
        print('[%s] error for url : %s' % (datetime.datetime.now(), url))
        pass
     
def getGeoData( address1, address2 ):
    url = 'https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc'
    aaa = urllib.parse.quote(address1)
    bbb = urllib.parse.quote(address2)
    url += '?request=coordsToaddr&coords=%s' % ( aaa + ',' + bbb )
    url += '&sourcecrs=epsg:4326&output=json&orders=admcode'
      
    result = get_request_url( url )
      
    if ( result == None ):
        print(address1+','+address2)
        return None 
    else :
        return json.loads( result ) # dict로 반환
     
mylist=[]
for idx in range(len(df_raw['longitude'])):
    lat=df_raw.iloc[idx]['latitude']
    long=df_raw.iloc[idx]['longitude']
    address2=str(lat)
    address1=str(long)
    jsonResult=getGeoData(address1, address2)
#     print(address2,address1)
#     print(jsonResult)
     
    jsonlist=jsonResult['results'][0]['region']
    sido=jsonlist['area1']['name']
    gu=jsonlist['area2']['name']
    dong=jsonlist['area3']['name']
#     print(sido,gu,dong)
     
     
    mylist.append((address2,address1,sido,gu,dong))
 
mycolumn=['latitude','longitude','sido','gu','dong']
  
myframe=DataFrame(mylist,columns=mycolumn)
  
filename='subway_all_2018.xlsx'
  
myframe.to_excel(filename,encoding='cp949')
print(filename+'저장완료')