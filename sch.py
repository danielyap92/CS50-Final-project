import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('car.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# spark plug

#Retrieving data
s = "2"
cursor.execute("SELECT spark_plug FROM periodic_service ORDER BY n DESC LIMIT ?", s)


#Fetching 1st row from the table
result = cursor.fetchall();
print(result)

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()