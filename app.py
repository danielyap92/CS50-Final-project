import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from helpers import response


app = Flask(__name__)
app.secret_key = '7d5bea5c9d554fd8e600d219768f06d860c43f5f280207e5d880ad0d8323d824'
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    conn = sqlite3.connect('car.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM periodic_service")
    res = cursor.fetchall();
    conn.close()

    histories = []

    for i in range (len(res)):
        sch =['n','engine_oil','engine_oil_filter','drain_plug_gasket','spark_plug','air_filter','radiator_coolant','brake_fluid','fuel_filter','transmission_oil_cvt','transmission_oil_filter','gasket_oil_pan','drain_plug','timing_belt_kit','fead_belt','datetime']
        # mod value start here
        mod1 = ["yes" if value == 1
            else value for value in res[i]]
        mod2 = [" " if value == 0
            else value for value in mod1]
        # mod value end here
        dic = dict(zip(sch,mod2))
        histories.append(dic)

    
    return render_template("index.html", histories=histories)
    
    

@app.route("/next_service", methods=["GET", "POST"])
def next_service():
    if request.method == "POST":
        list = request.form.getlist("service_checkbox")
    
        # generate SQL value from user response
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

        session['confirmation_list'] = nsil

        # replace word with underscore
        pricelist = {}
        for i in range(len(list)):
            if list[i] == 'engine_oil':
                pricelist.update({'Engine Oil': 100.00 })
            
            if list[i] == 'engine_oil_filter':
                pricelist.update({'Engine Oil Filter': 12.12 })
 
            if list[i] == 'drain_plug_gasket':
                pricelist.update({'Drain Plug Gasket': 3.02 })

            if list[i] == 'spark_plug':
                pricelist.update({'Spark Plug': 51.00 })
 
            if list[i] == 'air_filter':
                pricelist.update({'Air Filter': 16.35 })

            if list[i] == 'radiator_coolant':
                pricelist.update({'Radiator Coolant': 41.77 })
            
            if list[i] == 'brake_fluid':
                pricelist.update({'Brake Fluid': 36.20 })
 
            if list[i] == 'fuel_filter':
                pricelist.update({'Fuel Filter': 39.10 })

            if list[i] == 'transmission_oil_cvt':
                pricelist.update({'Transmission Oil CVT': 160.00 })

            if list[i] == 'transmission_oil_filter':
                pricelist.update({'Transmission Oil Filter': 156.12 })

            if list[i] == 'gasket_oil_pan':
                pricelist.update({'Gasket Oil Pan': 66.63 })
            
            if list[i] == 'drain_plug':
                pricelist.update({'Drain Plug': 26.28 })

            if list[i] == 'timing_belt_kit':
                pricelist.update({'Timing Belt Kit': 334.68 })

            if list[i] == 'fead_belt':
                pricelist.update({'FEAD Belt': 66.99 })
 
        return render_template("confirmation.html", pricelist = pricelist )

    else: 
        conn = sqlite3.connect('car.db')
        cursor = conn.cursor()
        prechecked_service_list = {}
        
        # Engine Oil: eveytime service
        def engine_oil():
                prechecked_service_list['engine_oil'] = 'checked'

        # Engine Oil filter: eveytime service
        def engine_oil_filter():
                prechecked_service_list['engine_oil_filter'] = 'checked'

        # Drain Plug Gasket: eveytime service
        def drain_plug_gasket():
                prechecked_service_list['drain_plug_gasket'] = 'checked'

        # Spark plug, f = how many frequency service once
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

        # Air Filter, f = how many frequency service once
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

        # Radiator Coolant, f = how many frequency service once
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

        # Brake fluid, f = how many frequency service once
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

        # Fuel filter, f = how many frequency service once
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

        # Transmission oil CVT, f = how many frequency service once
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

        # Transmission oil filter, f = how many frequency service once
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

        # Gasket oil pan, f = how many frequency service once
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

        # Drain plug, f = how many frequency service once
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

        # Timing Belt Kit, f = how many frequency service once
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

        # FEAD belt, f = how many frequency service once
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
        conn.close()
        return render_template("next_service.html", prechecked_service_list = prechecked_service_list)


@app.route("/confirmation", methods=["GET","POST"])
def confirmation():
    if request.method == "POST":
        conn = sqlite3.connect('car.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO periodic_service(engine_oil,engine_oil_filter,drain_plug_gasket,spark_plug,air_filter,radiator_coolant,brake_fluid,fuel_filter,transmission_oil_cvt,transmission_oil_filter,gasket_oil_pan,drain_plug,timing_belt_kit,fead_belt) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", session['confirmation_list'])
        conn.commit()
        conn.close()
        return response("Service record submitted !")
    else:
        return redirect("/next_service")
    


@app.route("/delete_record", methods=["GET","POST"])
def delete_record():
    if request.method == "POST":
        conn = sqlite3.connect('car.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM periodic_service WHERE n = (SELECT MAX(n) FROM periodic_service)")
        conn.commit()
        conn.close()
        return response("Service record deleted !")

    else:
        conn = sqlite3.connect('car.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM periodic_service WHERE n = (SELECT MAX(n) FROM periodic_service)")
        res = cursor.fetchall();
        conn.close()
        history = []
        for i in range (len(res)):
            sch =['n','engine_oil','engine_oil_filter','drain_plug_gasket','spark_plug','air_filter','radiator_coolant','brake_fluid','fuel_filter','transmission_oil_cvt','transmission_oil_filter','gasket_oil_pan','drain_plug','timing_belt_kit','fead_belt','datetime']
            # mod value start here
            mod1 = ["yes" if value == 1
                else value for value in res[i]]
            mod2 = [" " if value == 0
                else value for value in mod1]
            # mod value end here
            histories = dict(zip(sch,mod2))
            history.append(histories)
        return render_template("delete_record.html", history = history)

@app.route("/about_me")
def about_me():
    return render_template("about_me.html")

@app.route("/index")
def redirect_index():
    return redirect("/")
