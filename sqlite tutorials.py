import sqlite3 # importing sqlite in python which comes by default in Python3

conn = sqlite3.connect('tutorial.db') # create connections
c = conn.cursor()

# Create a table
def createTable():
    c.execute('CREATE TABLE IF NOT EXISTS stuff(name TEXT, phone REAL)')

def dataEntry():
    c.execute("INSERT INTO stuff VALUES('Aditya', 8882493410)")
    conn.commit() # to save or modify we do 'conn.commit'
    c.close() # close the cursor
    conn.close()

createTable()
dataEntry()
