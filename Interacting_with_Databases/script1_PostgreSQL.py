import py


"""
def create_table():
    
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT , quantity INTEGER , price REAL)")
    conn.commit()
    conn.close()

def insert_record(item , qty , price):

    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?, ? , ?)",(item , qty , price))
    conn.commit()
    conn.close()

#insert_record("Water Glass",10 , 10.5)
#insert_record("Coffee Glass",10 , 10.5)

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    #lite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 10 supplied
    #add comma afetr item
    cur.execute("DELETE FROM store WHERE item = ? " ,(item,))
    conn.commit()
    conn.close
  

delete('Wine Glass')

def upd(quantity , price , item ):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE  store SET quantity =? , price  = ? WHERE item = ?" ,(quantity , price , item ))
    conn.commit()
    conn.close

upd(20,20.5, 'Water Glass')
print(view())
"""
