import psycopg2

conn= psycopg2.connect(host='localhost',port='5432',user='postgres',password='Wafuladavid3422?',dbname='myduka_db')

#cursor object




cur=conn.cursor()
def get_data(sales):
    cur.execute(f"select*from sales")
    data=cur.fetchall()
    return data
data=get_data('SALES')
print(data)


def get_products():
    cur.execute("select*from products")
    products=cur.fetchall()
    return products
products=get_products()
print(products)


#cur.excute("insert into products(name,buying_price,selling_price)values('bread',60,70)")
conn.commit()
print(products)

def insert_products():
    cur.execute("insert into products(name,buying_price,selling_price)values('Bread',60,70)")
    conn.commit()