import pymysql

conn = pymysql.connect(host="localhost",port=3306,user="root",password="root",db="cos",charset="utf8")
cur = conn.cursor();
cur.execute("select link from jd_img limit 0,10");
data = cur.fetchall();
f = open("link.txt","a")
for item in data:
	f.write(item[0]+"\n")
f.close();