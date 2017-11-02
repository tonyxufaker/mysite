# -*- coding:utf-8 -*-
# 获取城市pm2.5排名
# Created by Tony Xu with Python 3.5 at 2017.10.31


from bs4 import BeautifulSoup
import requests
import sqlite3
from rank_city import city_list



def getPM25(cityname):
    #定义网站地址构成
    url = 'http://www.pm25.com/city/'+cityname+'.html'
    #发起网页请求
    html = requests.get(url)
    #用Beautifulsoup分析网页，获取网页内容
    soup = BeautifulSoup(html.text, 'html.parser')
    #解析城市中文名称
    city = soup.select('.city_name')[0].text
    #解析更新时间，因为爬取到的数据中含有更新时间字符，所以用replace替换掉
    updated_time = soup.select('.citydata_updatetime')[0].text.replace('更新时间：', '')
    #解析AQI指数
    AQI = soup.select('.cbol_aqi_num')[0].text
    #根据AQI指数，判断空气质量等级
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
    #解析污染物
    wuranwu = soup.select('.cbol_wuranwu_num ')[0].text
    #解析PM2.5
    PM25 = soup.select('.cbol_nongdu_num_1')[0].text
    #解析单位
    unit = soup.select('.cbol_nongdu_num_2')[0].text



    # 定义数据库路径
    db = r'E:\\pyproject\PM25\db.sqlite3'
    # 连接数据库，如果数据库不存在，则创建一个
    conn = sqlite3.connect(db)
    cusor = conn.cursor()
    #执行数据库操作：插入数据
    cusor.execute("SELECT * FROM PM_CITY WHERE (city='%s' AND updated_time='%s')"% (city, updated_time))
    result = cusor.fetchall()
    if len(result)>0:
        print("数据 %s %s 已存在" % (city, updated_time) )
        return
    else:
        cusor.execute("INSERT INTO PM_City (city, AQI, wuranwu, PM25, unit, level, updated_time) VALUES ('%s', %d, '%s', %d, '%s', '%s', '%s')" % (city, int(AQI), wuranwu, int(PM25), unit, level, updated_time))
        print("数据 %s %s插入成功！" % (city, updated_time))
    #提交数据库操作
    conn.commit()
    #关闭数据库链接
    conn.close()


#根据城市列表爬取各城市的PM2.5数据
def one_thread():
    for cityname in city_list:
        getPM25(cityname)






