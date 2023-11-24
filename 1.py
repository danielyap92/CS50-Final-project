lists = ['engine_oil', 'engine_oil_filter']
price = {}
for i in range(len(lists)):
    if lists[i] == 'engine_oil':
        lists[i] = 'Engine Oil'
        price.update({'Engine Oil': 100 })

    if lists[i] == 'engine_oil_filter':
        lists[i] = 'Engine Oil Filter'
        price.update({'Engine Oil Filter': 33.12 })

    if lists[i] == 'drain_plug_gasket':
        lists[i] = 'Drain Plug Gasket'
        price.update({'drain_plug_gasket': 80})

print(price)
total = sum(price.values())
print(total)