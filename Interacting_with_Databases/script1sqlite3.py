import sqlite3

# Connect to DB 
conn = sqlite3.connect("lite.db")


# Create a Cursor 
cur = conn.cursor()

# Write an SQl Query 

cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT , quantity INTEGER , price REAL)")

cur.execute("INSERT INTO store VALUES('Wine Glass', 8 , 10.5)")

# Commit Chnages 

conn.commit()
# Close Connectiom 

conn.close()

