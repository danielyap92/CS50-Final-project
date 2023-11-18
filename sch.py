import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('car.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

cursor.execute("SELECT max(n) FROM periodic_service")
n = cursor.fetchall();
print(n)


# spark plug

#Retrieving data
# f = how many frequency service once
f = 3 
s = str(f-1)


cursor.execute("SELECT spark_plug FROM periodic_service ORDER BY n DESC LIMIT ?", s)
result = cursor.fetchall();
z = [sum(t) for t in result]
print (z)
total = 0
for element in z:
    total += element
print(total)
# z = str(result)
# print (z)
# z1=re.sub['[(]','',z]
# print (z1)

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()