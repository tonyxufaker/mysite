# -*-encoding:utf-8-*-

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pymysql
import time
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

font = FontProperties(fname=r'c:\windows\Fonts\msyh.ttc', size=14)


def drawLineChart(city):
	# 加载数据
	time_now = time.strftime('%Y-%m-%d', time.localtime(time.time()))

	# 连接MySQL数据库
	connect = pymysql.connect(
		host='594cda6e75bf6.sh.cdb.myqcloud.com',
		port=5369,
		user='root',
		passwd='xt628510',
		db='main',
		charset='utf8'
	)
	cusor = connect.cursor()
	cusor.execute("SELECT AQI FROM PM_city WHERE city='{:s}' AND updated_time LIKE '{:s}%'".format(city, time_now))
	AQI = cusor.fetchall()
	cusor.execute(
		"SELECT updated_time FROM PM_city WHERE city='{:s}' AND updated_time LIKE '{:s}%'".format(city, time_now))
	updated_time = cusor.fetchall()
	# 提交数据库操作
	connect.commit()
	# 关闭数据库链接
	connect.close()

	# 绘画
	x = []
	for xx in updated_time:
		xxx = time.strptime(str(xx).replace('(', '').replace(')', '').replace("'", '').replace(',', ''),
							"%Y-%m-%d %H:%M")
		x.append(xxx.tm_hour)
	mpl.rcParams['xtick.labelsize'] = 12
	mpl.rcParams['ytick.labelsize'] = 10
	ymajorLocator = MultipleLocator(5)
	xmajorLocator = MultipleLocator(2)

	y = []
	for yy in AQI:
		yyy = int(str(yy).replace('(', '').replace(')', '').replace("'", '').replace(',', ''))
		y.append(yyy)

	arr = np.array([x, y])
	plt.figure('{:s}空气质量变化趋势 {:s}'.format(city, time_now))

	plt.ylabel(u'AQI指数', fontproperties=font)
	plt.xlabel(u'小时', fontproperties=font)
	plt.plot(arr[0], arr[1], '')

	ax = plt.subplot(111)
	ax.xaxis.set_major_locator(xmajorLocator)
	ax.yaxis.set_major_locator(ymajorLocator)
	ax.xaxis.grid(True, which='major')
	ax.yaxis.grid(True, which='major')
	img_url = "static\img\ChartLine_{:s}_{:s}.png".format(city, time_now)
	plt.savefig(img_url, dpi=150)
	return img_url



if __name__ == '__main__':
	city = input('请输入城市名称：')
	drawLineChart(city)






