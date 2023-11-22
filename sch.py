import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('car.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

cursor.execute("SELECT max(n) FROM periodic_service")
n = cursor.fetchall();
n1 = [sum(t) for t in n]
last_number_of_service = int(''.join(map(str, n1)))
# print("Last number of service: " + str(last_number_of_service))

current_number_service = last_number_of_service + 1
# print ("Current number of service: " + str(current_number_service))

prechecked_service_list ={}

# Engine Oil
# Eveytime service
def engine_oil():
        prechecked_service_list['engine_oil'] = 'checked'

# Engine Oil filter
# Eveytime service
def engine_oil_filter():
        prechecked_service_list['engine_oil_filter'] = 'checked'

# Drain Plug Gasket
# Eveytime service
def drain_plug_gasket():
        prechecked_service_list['drain_plug_gasket'] = 'checked'


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
        prechecked_service_list['spark_plug'] = 'checked'
    else:
        prechecked_service_list['spark_plug'] = 'unchecked'

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
        prechecked_service_list['air_filter'] = 'checked'
    else:
        prechecked_service_list['air_filter'] = 'unchecked'

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
        prechecked_service_list['radiator_coolant'] = 'checked'
    else:
        prechecked_service_list['radiator_coolant'] = 'unchecked'

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
        prechecked_service_list['brake_fluid'] = 'checked'
    else:
        prechecked_service_list['brake_fluid'] = 'unchecked'

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
        prechecked_service_list['fuel_filter'] = 'checked'
    else:
        prechecked_service_list['fuel_filter'] = 'unchecked'

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
        prechecked_service_list['transmission_oil_cvt'] = 'checked'
    else:
        prechecked_service_list['transmission_oil_cvt'] = 'unchecked'

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
        prechecked_service_list['transmission_oil_filter'] = 'checked'
    else:
        prechecked_service_list['transmission_oil_filter'] = 'unchecked'

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
        prechecked_service_list['gasket_oil_pan'] = 'checked'
    else:
        prechecked_service_list['gasket_oil_pan'] = 'unchecked'

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
        prechecked_service_list['drain_plug'] = 'checked'
    else:
        prechecked_service_list['drain_plug'] = 'unchecked'

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
        prechecked_service_list['timing_belt_kit'] = 'checked'
    else:
        prechecked_service_list['timing_belt_kit'] = 'unchecked'

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
        prechecked_service_list['fead_belt'] = 'checked'
    else:
        prechecked_service_list['fead_belt'] = 'unchecked'

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
fead_belt()


#filter no need service
# def filter_service(pair):
#      key, value = pair
#      if value == 1:
#         return True
#      else:
#           return False

# def current_service_list():
#     service_list = dict(filter(filter_service, prechecked_service_list.items()))
#     print (service_list)

# current_service_list()


#Commit your changes in the database
#conn.commit()

#Closing the connection
conn.close()