import psycopg2
# 1. connect to a db
# 2. create a cursor object
# 3. write an SQL query
# 4. commit changes
# 5. ckise db connection
def create_table():
    conn=psycopg2.connect("dbname= 'database1' user='postgres' password='postgres123' host='localhost' port='5432'") #main difference
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, qunatity, price):
    conn=psycopg2.connect("dbname= 'database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    # cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item, qunatity, price))
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)",(item, qunatity, price))
    conn.commit()
    conn.close()

#insert("Coffee Cup",10,5)

def view():
    conn=psycopg2.connect("dbname= 'database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname= 'database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,)) # use %s instead of ?
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=psycopg2.connect("dbname= 'database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()

create_table()
#insert("Orange",10,15)
update(20,15,"Apple")
delete("Orange")
print(view())
