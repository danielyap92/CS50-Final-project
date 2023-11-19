import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('car.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

cursor.execute("SELECT max(n) FROM periodic_service")
n = cursor.fetchall();
n1 = [sum(t) for t in n]
last_number_of_service = int(''.join(map(str, n1)))
print("Last number of service: " + str(last_number_of_service))

current_number_service = last_number_of_service + 1
print ("Current number of service: " + str(current_number_service))

current_service_dict ={}

# Engine Oil
# Eveytime service
def engine_oil():
        current_service_dict['engine_oil'] = 1

# Engine Oil filter
# Eveytime service
def engine_oil_filter():
        current_service_dict['engine_oil_filter'] = 1

# Drain Plug Gasket
# Eveytime service
def drain_plug_gasket():
        current_service_dict['drain_plug_gasket'] = 1


# Spark plug
# f = how many frequency service once
def spark_plug():
    f = 3 
    s = f - 1
    cursor.execute("SELECT spark_plug FROM periodic_service ORDER BY n DESC LIMIT ?", (s,))
    result = cursor.fetchall();
    z = [sum(t) for t in result]
    total = 0
    for element in z:
        total += element
    if total == 0:
        current_service_dict['spark_plug'] = 1
    else:
        current_service_dict['spark_plug'] = 0

# Air Filter
# f = how many frequency service once
def air_filter():
    f = 2 
    s = f - 1
    cursor.execute("SELECT air_filter FROM periodic_service ORDER BY n DESC LIMIT ?", (s,))
    result = cursor.fetchall();
    z = [sum(t) for t in result]
    total = 0
    for element in z:
        total += element
    if total == 0:
        current_service_dict['air_filter'] = 1
    else:
        current_service_dict['air_filter'] = 0

# Radiator Coolant
# f = how many frequency service once
def radiator_coolant():
    f = 9 
    s = f - 1
    cursor.execute("SELECT radiator_coolant FROM periodic_service ORDER BY n DESC LIMIT ?", (s,))
    result = cursor.fetchall();
    z = [sum(t) for t in result]
    total = 0
    for element in z:
        total += element
    if total == 0:
        current_service_dict['radiator_coolant'] = 1
    else:
        current_service_dict['raidator_coolant'] = 0

# Brake fluid
# f = how many frequency service once
def brake_fluid():
    f = 4 
    s = f - 1
    cursor.execute("SELECT brake_fluid FROM periodic_service ORDER BY n DESC LIMIT ?", (s,))
    result = cursor.fetchall();
    z = [sum(t) for t in result]
    total = 0
    for element in z:
        total += element
    if total == 0:
        current_service_dict['brake_fluid'] = 1
    else:
        current_service_dict['brake_fluid'] = 0

# Fuel filter
# f = how many frequency service once
def fuel_filter():
    f = 3 
    s = f - 1
    cursor.execute("SELECT fuel_filter FROM periodic_service ORDER BY n DESC LIMIT ?", (s,))
    result = cursor.fetchall();
    z = [sum(t) for t in result]
    total = 0
    for element in z:
        total += element
    if total == 0:
        current_service_dict['fuel_filter'] = 1
    else:
        current_service_dict['fuel_filter'] = 0

# Transmission oil CVT
# f = how many frequency service once
def transmission_oil_cvt():
    f = 6 
    s = f - 1
    cursor.execute("SELECT transmission_oil_cvt FROM periodic_service ORDER BY n DESC LIMIT ?", (s,))
    result = cursor.fetchall();
    z = [sum(t) for t in result]
    total = 0
    for element in z:
        total += element
    if total == 0:
        current_service_dict['transmission_oil_cvt'] = 1
    else:
        current_service_dict['transmission_oil_cvt'] = 0

# Transmission oil filter
# f = how many frequency service once
def transmission_oil_filter():
    f = 6 
    s = f - 1
    cursor.execute("SELECT transmission_oil_filter FROM periodic_service ORDER BY n DESC LIMIT ?", (s,))
    result = cursor.fetchall();
    z = [sum(t) for t in result]
    total = 0
    for element in z:
        total += element
    if total == 0:
        current_service_dict['transmission_oil_filter'] = 1
    else:
        current_service_dict['transmission_oil_filter'] = 0

# Gasket oil pan
# f = how many frequency service once
def gasket_oil_pan():
    f = 12 
    s = f - 1
    cursor.execute("SELECT gasket_oil_pan FROM periodic_service ORDER BY n DESC LIMIT ?", (s,))
    result = cursor.fetchall();
    z = [sum(t) for t in result]
    total = 0
    for element in z:
        total += element
    if total == 0:
        current_service_dict['gasket_oil_pan'] = 1
    else:
        current_service_dict['gasket_oil_pan'] = 0

# Drain plug
# f = how many frequency service once
def drain_plug():
    f = 6 
    s = f - 1
    cursor.execute("SELECT drain_plug FROM periodic_service ORDER BY n DESC LIMIT ?", (s,))
    result = cursor.fetchall();
    z = [sum(t) for t in result]
    total = 0
    for element in z:
        total += element
    if total == 0:
        current_service_dict['drain_plug'] = 1
    else:
        current_service_dict['drain_plug'] = 0

# Timing Belt Kit
# f = how many frequency service once
def timing_belt_kit():
    f = 11 
    s = f - 1
    cursor.execute("SELECT timing_belt_kit FROM periodic_service ORDER BY n DESC LIMIT ?", (s,))
    result = cursor.fetchall();
    z = [sum(t) for t in result]
    total = 0
    for element in z:
        total += element
    if total == 0:
        current_service_dict['timing_belt_kit'] = 1
    else:
        current_service_dict['timing_belt_kit'] = 0

# FEAD belt
# f = how many frequency service once
def fead_belt():
    f = 10 
    s = f - 1
    cursor.execute("SELECT fead_belt FROM periodic_service ORDER BY n DESC LIMIT ?", (s,))
    result = cursor.fetchall();
    z = [sum(t) for t in result]
    total = 0
    for element in z:
        total += element
    if total == 0:
        current_service_dict['fead_belt'] = 1
    else:
        current_service_dict['timing_belt_kit'] = 0

engine_oil()
engine_oil_filter()
drain_plug_gasket()
spark_plug()
air_filter()
radiator_coolant()
brake_fluid()
fuel_filter()
transmission_oil_cvt()
transmission_oil_filter()
gasket_oil_pan()
drain_plug()
timing_belt_kit()
# print (current_service_dict)
# print ('After filter not need to service')

def filter_service(pair):
     key, value = pair
     if value == 1:
        return True
     else:
          return False

def current_service_list():
    service_list = dict(filter(filter_service, current_service_dict.items()))
    print (service_list)

current_service_list()


#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()