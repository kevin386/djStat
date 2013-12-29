#-*- coding:utf8 -*-
#统一数据库内容所有表项的编码
import MySQLdb

host = "localhost"
passwd = "123456"
user = "root"
dbname = "pydb"

db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=dbname)
cursor = db.cursor()

cursor.execute("show variables like 'character_%'")
for i in cursor.fetchall():
	print i
cursor.execute("show variables like 'collation_%'")

cursor.execute("ALTER DATABASE `%s` CHARACTER SET 'utf8' COLLATE 'utf8_unicode_ci'" % dbname)

sql = "SELECT DISTINCT(table_name) FROM information_schema.columns WHERE table_schema = '%s'" % dbname
cursor.execute(sql)

results = cursor.fetchall()
for row in results:
    sql = "ALTER TABLE `%s` convert to character set DEFAULT COLLATE DEFAULT" % (row[0])
    cursor.execute(sql)
db.close()
