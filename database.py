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
curr=conn.cursor()
def insert_sales(values):
   query='Insert into sales (pid,quantity,created_at)values(%s,%s,now());'
   cur.execute(query,values)
   conn.commit()

#fetch data sales per product
# use inner join for sales and product,product is parent,child is sales
def product_sales():
    querry='select productname,productid,sum(selling_price*quantity) as total_sales from sales  inner join products on productid.sales=productid.products group by productname,productid;'
    cur.execute(querry)
    sales=cur.fetchall()
    return sales
mysale=product_sales()
print(mysale)
#sales per day
def sales_per_day():
    create_script='select sum (selling_price*quantity) as total_sales from sales inner join products on sales.productid=products.productid;'
    cur.execute(create_script)
    sales=cur.fetchall()
    return sales
sales=sales_per_day()
print(sales)



