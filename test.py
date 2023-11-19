import sqlite3

conn = sqlite3.connect('car.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM periodic_service")
res = cursor.fetchall();
print(len(res))

car_dict = []

for i in range (len(res)):
    sch =['n','engine_oil','engine_oil_filter','drain_plug_gasket','spark_plug','air_filter','radiator_coolant','brake_fluid','fuel_filter','transmission_oil_cvt','transmission_oil_filter','gasket_oil_pan','drain_plug','timing_belt_kit']
    dic = dict(zip(sch,res[i]))
    car_dict.append(dic)


print(car_dict[0]['n'])


# previous_service_list = []

# for row in res:
#     i = 0
#     print(i)
#     print(res[i])
#     i = i + 1

    # previous_service_list.append(
    #     {
    #         'engine_oil': row['engine_oil'],
    #         'engine_oil_filter': row['engine_oil_filter']
    #     }
    # )

# print(previous_service_list)
conn.close()