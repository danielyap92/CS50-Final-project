import sqlite3

conn = sqlite3.connect('car.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM periodic_service")
res = cursor.fetchall();


# print(len(res))

# mod = ["yes" if value == 1
#        else value for value in res[0]]
# mod = [" " if value == 0
#        else value for value in mod]
# print(mod)

car_dict = []

for i in range (len(res)):
    sch = ['n','engine_oil','engine_oil_filter','drain_plug_gasket','spark_plug','air_filter','radiator_coolant','brake_fluid','fuel_filter','transmission_oil_cvt','transmission_oil_filter','gasket_oil_pan','drain_plug','timing_belt_kit']
    # mod value start here
    mod1 = ["yes" if value == 1
        else value for value in res[i]]
    mod2 = [" " if value == 0
        else value for value in mod1]
    # mod value end here
    dic = dict(zip(sch,mod2))
    car_dict.append(dic)
print(car_dict)



conn.close()