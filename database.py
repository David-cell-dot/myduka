import psycopg2

conn= psycopg2.connect(host='localhost',port='5432',user='postgres',password='Wafuladavid3422?',dbname='myduka_db')
#CURSOR OBJECT
cur=conn.cursor()
def get_data(table):
    cur.execute(f"select*from sales")
    data=cur.fetchall()
    return data

data=get_data('sales')
print(data)


def get_products():
    cur.execute("select*from products")
    products=cur.fetchall()
    return products

products=get_products()
print(products)


cur.execute("insert into products(name,buying_price,selling_price)values('bread',50,60)")
conn.commit()
print(products)

def inser_products():
    cur.execute("insert into products(name,buying_price,selling_price)values('bread',50,60)")
conn.commit()

