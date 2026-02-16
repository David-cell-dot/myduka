import psycopg2

conn= psycopg2.connect(host='localhost',port='5432',user='postgres',password='Wafuladavid3422?',dbname='myduka_db')
#CURSOR OBJEct



cur=conn.cursor()
def get_data(table):
    cur.execute(f"select*from {table}")
    data=cur.fetchall()
    return data

data=get_data('sales')
print(data)


def get_products():
    cur.execute("select*from products;")
    products=cur.fetchall()
    return products

products=get_products()
print(products)


def fetch_stock():
    cur.execute("select*from stock;")
    stock=cur.fetchall()
    return stock
stock1=fetch_stock()
print(stock1)


cur.execute("insert into products(name,buying_price,selling_price)values('bread',50,60)")
conn.commit()
print(products)

def insert_products():
    cur.execute(f"insert into products(name,buying_price,selling_price)values('bread',50,60)")
conn.commit()




def insert_products(values):
    cur.execute(f"insert into products(name,buying_price,selling_price) values{values}")
    conn.commit()

product1=('samsung',20000,30000)
product2=('hp',30000,40000)

insert_products(product1)
insert_products(product2)


#fetch data fro sales
def get_sales():
    cur.execute("select*from sales;")
    sales=cur.fetchall()
    return sales
sales=get_sales()
print(sales)

#insert sales
def insert_sales(values):
   cur.execute(f"insert into sales(pid,quantity)values{values}")
   conn.commit()
   sales1=(20,2)
   sales2=(20,2)

   insert_sales(sales1)
   insert_sales(sales2)

   
   









  



