import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('car.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

cursor.execute("SELECT max(n) FROM periodic_service")
n = cursor.fetchall();
print(n)

sdict ={}

# Engine Oil
# Eveytime service
def engine_oil():
        sdict['engine_oil'] = 1

# Engine Oil filter
# Eveytime service
def engine_oil_filter():
        sdict['engine_oil_filter'] = 1

# Drain Plug Gasket
# Eveytime service
def drain_plug_gasket():
        sdict['drain_plug_gasket'] = 1


# Spark plug
# f = how many frequency service once
def spark_plug():
    f = 3 
    s = str(f-1)
    cursor.execute("SELECT spark_plug FROM periodic_service ORDER BY n DESC LIMIT ?", s)
    result = cursor.fetchall();
    z = [sum(t) for t in result]
    total = 0
    for element in z:
        total += element
    print('total is ' + str(total))
    if total == 0:
        sdict['spark_plug'] = 1
    else:
        sdict['spark_plug'] = 0

# Spark plug
# f = how many frequency service once
def air_filter():
    f = 2 
    s = str(f-1)
    cursor.execute("SELECT air_filter FROM periodic_service ORDER BY n DESC LIMIT ?", s)
    result = cursor.fetchall();
    z = [sum(t) for t in result]
    total = 0
    for element in z:
        total += element
    print('total is ' + str(total))
    if total == 0:
        sdict['air_filter'] = 1
    else:
        sdict['air_filter'] = 0

engine_oil()
engine_oil_filter()
drain_plug_gasket()
spark_plug()
air_filter()
print (sdict)
print ('After filter not need to service')
def filter_service(pair):
     key, value = pair
     if value == 1:
        return True
     else:
          return False
service_list = dict(filter(filter_service, sdict.items()))
print (service_list)

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()