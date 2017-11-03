# -*-encoding:utf-8-*-



import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import sqlite3
import time, datetime

font = FontProperties(fname=r'c:\windows\Fonts\msyh.ttc', size=14)

#加载数据

city = input('请输入城市名称：')
time_now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# 定义数据库路径
db = r'db.sqlite3'
# 连接数据库
conn = sqlite3.connect(db)
cusor = conn.cursor()
cusor.execute("SELECT AQI FROM PM_CITY WHERE city='{:s}' AND updated_time LIKE '{:s}%'".format(city, time_now))
AQI = cusor.fetchall()
cusor.execute(
"SELECT updated_time FROM PM_CITY WHERE city='{:s}' AND updated_time LIKE '{:s}%'".format(city, time_now))
updated_time = cusor.fetchall()
# 提交数据库操作
conn.commit()
# 关闭数据库链接
conn.close()




#绘画
x = []
for xx in updated_time:
	xxx = time.strptime(str(xx).replace('(', '').replace(')', '').replace("'", '').replace(',', ''),
							"%Y-%m-%d %H:%M")
	x.append(xxx.tm_hour)
mpl.rcParams['xtick.labelsize'] = 12
mpl.rcParams['ytick.labelsize'] = 10

plt.figure('{:s}空气质量变化趋势 {:s}'.format(city, time_now))

plt.ylabel(u'AQI指数', fontproperties=font)
plt.xlabel(u'小时', fontproperties=font)
plt.plot(x, AQI, '')
plt.show()






