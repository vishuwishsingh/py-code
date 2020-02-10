import psycopg2



def create_table():
    
    conn = psycopg2.connect("dbname = 'database1' user='postgres' password='12345678' host='127.0.0.1' port='5499'" )
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT , quantity INTEGER , price REAL)")
    conn.commit()
    conn.close()

create_table()    

def insert_record(item , qty , price):

    conn = psycopg2.connect("dbname = 'database1' user='postgres' password='12345678' host='127.0.0.1' port='5499'" )
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s, %s , %s)",(item , qty , price))
    conn.commit()
    conn.close()

#insert_record("Water Glass",10 , 10.5)
#insert_record("Coffee Glass",10 , 10.5)

def view():
    conn = psycopg2.connect("dbname = 'database1' user='postgres' password='12345678' host='127.0.0.1' port='5499'" )
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close
    return rows

def delete(item):
    conn = psycopg2.connect("dbname = 'database1' user='postgres' password='12345678' host='127.0.0.1' port='5499'" )
    cur = conn.cursor()
    #lite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 10 supplied
    #add comma afetr item
    cur.execute("DELETE FROM store WHERE item = %s " ,(item,))
    conn.commit()
    conn.close
  



def upd(quantity , price , item ):
    conn = psycopg2.connect("dbname = 'database1' user='postgres' password='12345678' host='127.0.0.1' port='5499'" )
    cur = conn.cursor()
    cur.execute("UPDATE  store SET quantity =%s , price  = %s WHERE item = %s" ,(quantity , price , item ))
    conn.commit()
    conn.close

delete('Water Glass')
upd(20,20.5, 'Coffee Glass')
print(view())

