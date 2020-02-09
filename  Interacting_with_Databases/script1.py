import sqlite3

# Connect to DB 
conn = sqlite3.connect("lite.db")


# Create a Cursor 
cur = conn.cursor()

# Write an SQl Query 

cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT , quantity INTEGER , price REAL)")

# Commit Chnages 

conn.commit()
# Close Connectiom 

conn.close()

