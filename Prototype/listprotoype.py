list = ['engine_oil', 'engine_oil_filter', 'timing_belt_kit', 'fead_belt']

nsil = []


if 'engine_oil' in list:
    nsil.append(1)
else:
    nsil.append(0)

if 'engine_oil_filter' in list:
    nsil.append(1)
else:
    nsil.append(0)

if 'drain_plug_gasket' in list:
    nsil.append(1)
else:
    nsil.append(0)

if 'spark_plug' in list:
    nsil.append(1)
else:
    nsil.append(0)

if 'air_filter' in list:
    nsil.append(1)
else:
    nsil.append(0)

if 'radiator_coolant' in list:
    nsil.append(1)
else:
    nsil.append(0)

if 'brake_fluid' in list:
    nsil.append(1)
else:
    nsil.append(0)

if 'fuel_filter' in list:
    nsil.append(1)
else:
    nsil.append(0)

if 'transmission_oil_cvt' in list:
    nsil.append(1)
else:
    nsil.append(0)

if 'transmission_oil_filter' in list:
    nsil.append(1)
else:
    nsil.append(0)

if 'gasket_oil_pan' in list:
    nsil.append(1)
else:
    nsil.append(0)

if 'drain_plug' in list:
    nsil.append(1)
else:
    nsil.append(0)

if 'timing_belt_kit' in list:
    nsil.append(1)
else:
    nsil.append(0)

if 'fead_belt' in list:
    nsil.append(1)
else:
    nsil.append(0)


print(nsil)