import sqlite3

conn = sqlite3.connect('car.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM periodic_service")
res = cursor.fetchall();


print(res[0][0])

mod = ["yes" if value == 1
       else value for value in res[0]]
mod = ["no" if value == 0
       else value for value in mod]
print(mod)

# car_dict = []

# for i in range (len(res)):
#     sch =['n','engine_oil','engine_oil_filter','drain_plug_gasket','spark_plug','air_filter','radiator_coolant','brake_fluid','fuel_filter','transmission_oil_cvt','transmission_oil_filter','gasket_oil_pan','drain_plug','timing_belt_kit']
#     dic = dict(zip(sch,res[i]))
#     car_dict.append(dic)

# history = ["✔" if svs == 0 
#            else svs for svs in car_dict]

# print(history)



conn.close()