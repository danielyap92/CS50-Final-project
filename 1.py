import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('car.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving data
cursor.execute('''SELECT * FROM periodic_service''')

#Fetching 1st row from the table
# result = cursor.fetchone();
# print(result)

#Fetching 1st row from the table
result = cursor.fetchall();
print(result)

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()