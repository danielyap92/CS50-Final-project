import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('car.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()



current_service_dict ={}


# Spark plug
# f = how many frequency service once


def periodic(): 
    cursor.execute("SELECT spark_plug FROM periodic_service ORDER BY n DESC LIMIT ?", '10' )
    result = cursor.fetchall();
    print(result)
    # z = [sum(t) for t in result]
    # total = 0
    # for element in z:
    #     total += element
    # if total == 0:
    #     current_service_dict['spark_plug'] = 1
    # else:
    #     current_service_dict['spark_plug'] = 0
    # print(current_service_dict)

periodic()





#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()