# -*- coding:utf-8 -*-
# 获取城市pm2.5排名
# Created by Tony Xu with Python 3.5 at 2017.10.31


from bs4 import BeautifulSoup
import requests
from time import ctime
import threading
import sqlite3



def getPM25(cityname):
    url = 'http://www.pm25.com/city/'+cityname+'.html'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    city = soup.select('.city_name')[0].text
    updated_time = soup.select('.citydata_updatetime')[0].text
    AQI = soup.select('.cbol_aqi_num')[0].text
    AQI_num = int(AQI)
    if AQI_num >= 50:
        if AQI_num >=100:
            if AQI_num >= 150:
                if AQI_num >= 200:
                    if AQI_num >= 300:
                        if AQI_num >= 500:
                            level = '严重污染'
                        else:
                            level = '严重污染'
                    else:
                        level = '重度污染'
                else:
                    level= '中度污染'
            else:
                level = '轻度污染'
        else:
            level = '良'
    else:
        level = '优'
    wuranwu = soup.select('.cbol_wuranwu_num ')[0].text
    PM25 = soup.select('.cbol_nongdu_num_1')[0].text
    unit = soup.select('.cbol_nongdu_num_2')[0].text
    print(city+'\n'+updated_time+'\n'+'AQI指数：'+AQI+'\n'+"首要污染物："+wuranwu+'\n'+'PM25：'+PM25+unit+'\n'+'空气质量等级：'+level+'\n'+'查询时间：'+ctime())

    #连接数据库，如果数据库不存在，则创建一个
    conn = sqlite3.connect('E:\pyproject\PM25\db.sqlite3\main.db')
    cusor = conn.cursor()
    cusor.execute("INSERT INTO PM_City (city, AQI, wuranwu, PM25, unit, level, updated_time) VALUES ('%s', %d, '%s', %d, '%s', '%s', '%s')")
    conn.commit()
    conn.close()


def one_thread():
    cn = input('请输入城市名称拼音：')
    getPM25(cn)

def two_thread():
    threads = []
    cn1 = input('请输入城市名称拼音：')
    cn2 = input('请输入城市名称拼音：')
    t1 = threading.Thread(target=getPM25, args=cn1)
    threads.append(t1)
    t2 = threading.Thread(target=getPM25, args=cn2)
    threads.append(t2)

    for t in threads:
        t.start()

if __name__ == '__main__':
    one_thread()
    print('\n\n')
    two_thread()




