import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456789"
)

db=mydb.cursor()
db.execute("use showroom")

db.execute("select model_name from model where model_id in (1,2)")
re=db.fetchall()
print(re)
a=re[0]
print(a)
for i in a:
     print(i[1])
