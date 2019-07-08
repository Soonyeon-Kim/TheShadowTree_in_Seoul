from selenium import webdriver
from bs4 import BeautifulSoup
from project1.calendertest import date_cal
import pandas as pd


def date_preclean(date_list, time_list):
    return_date = []
    for item in date_list:
        for item2 in time_list:
            inputdata = item+' '+item2
            return_date.append(inputdata)
    return return_date
        
html = 'https://www.weather.go.kr/weather/observation/aws_table_popup.jsp'
iframe_id = 'menu'
frame_name = 'disp'

driver = webdriver.Chrome('C:/Users/TJ/Downloads/chromedriver_win32/chromedriver.exe')



driver.get(html)
iframes = driver.find_elements_by_css_selector('iframe')
for iframe in iframes:
    print(iframe.get_attribute('name'))
driver.switch_to_frame('menu')
page_source2 = driver.page_source
soup = BeautifulSoup(page_source2, 'lxml') 
body = soup.find('body')
aa = driver.find_element_by_xpath("//option[@value='"+ 'MINDB_60M'+"']")
aa.click()
 
# 필요시간
time_list = ['13:00','14:00','15:00']
 
#날짜 산정
start_date_2017 = '2017-06-20'
end_date_2017 = '2017-08-31'
datelist_2017 = date_cal(start_date_2017,end_date_2017)

start_date_2018 = '2018-06-20'
end_date_2018 = '2018-08-31'
datelist_2018 = date_cal(start_date_2018,end_date_2018)
datelist = datelist_2017 + datelist_2018
#datelist = date_cal('2018-03-01', '2018-03-02')
# 최종 날짜 시간 리스트
result_date = []

result_date_2017 = date_preclean(datelist_2017, time_list)
result_date_2018 = date_preclean(datelist_2018, time_list)
result_date = result_date_2017 + result_date_2018



# 최종 데이터 리스트
result = []

#date에 따른 크롤링 시작
for date in result_date:
    driver.switch_to_default_content()
    input_date = driver.find_element_by_id('datecal2')
    # 지우기
    input_date.clear()
    input_date.send_keys(date)
    driver.find_element_by_xpath('//*[@id="frm"]/table/tbody/tr/td[2]/input').click()
    #포문 열고 result_date 다 쓸때까지... 프레임전환도 각자각자
    #프레임 상위 전환
    driver.switch_to_default_content()
    #프레임 자식으로 파고들어가기
    driver.switch_to_frame('disp')
    driver.switch_to_frame('body')
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    #프레임 내의 태그 처리 
    notices = soup.find('tbody')
    notices2 = notices.find('tbody')
    head_list = []
    temper_list = []
    for item in notices2.find_all('tr', {'class':'text'}):
        count = 0
        for item2 in item.find_all('td'):
            count += 1
            if(count==2):
                if(item2.text[-1] == '*'):
                    r_name = item2.text.replace(' *', '')       
                    head_list.append(r_name)
                else:   
                    head_list.append(item2.text)
            elif(count==11):
                temper_list.append(item2.text)
    result.append(temper_list)
           
#dataframe화 시켜서 csv로 저장

data = pd.DataFrame(result)
data.columns = head_list
data.to_csv('온도크롤링.csv', encoding='cp949')

print('finished')

