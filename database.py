import psycopg2

conn= psycopg2.connect(host='localhost',port='5432',user='postgres',password='6979',dbname='myduka_db')
#CURSOR OBJECT
cur=conn.cursor()
cur.excute("select* from products")
products=cur.fetchall()
print(products)