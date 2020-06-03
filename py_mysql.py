import pymysql
#获取数据库
db = pymysql.connect(host='localhost',port = 3306,user='root',password='linlisen',database='stu',charset='utf8')






#获取游标`
cur=db.cursor()
#数据操作







#关闭游标和数据库连接
cur.close()
db.close()
