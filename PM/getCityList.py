import pymysql



# 获取数据库中所有的城市名称
def GetCityList():
	# 连接mysql数据库
	connect = pymysql.connect(
		host='594cda6e75bf6.sh.cdb.myqcloud.com',
		port=5369,
		user='root',
		passwd='xt628510',
		db='main',
		charset='utf8'
	)
	cursor = connect.cursor()
	cursor.execute(
		"SELECT city FROM PM_city"
	)
	List = cursor.fetchall()
	cityList = []
	for list in List:
		s = str(list).replace('(', '').replace(')', '').replace(',', '').replace("'", '')
		cityList.append(s)
	return cityList


if __name__ == '__main__':
	GetCityList()
	#print(GetCityList())