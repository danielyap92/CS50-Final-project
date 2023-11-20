list1 = ['engine_oil', 'engine_oil_filter', 'drain_plug_gasket', 'air_filter', 'brake_fluid']
list = ['engine_oil', 'engine_oil_filter']

list2 = []

if 'engine_oil' in list:
    list2.append(1)
else:
    list2.append(0)

if 'engine_oil_filter' in list:
    list2.append(1)
else:
    list2.append(0)

if 'drain_plug_gasket' in list:
    list2.append(1)
else:
    list2.append(0)

print(list2)