# import os
import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from sch import last_number_of_service, current_number_service, prechecked_service_list


app = Flask(__name__)
app.secret_key = '7d5bea5c9d554fd8e600d219768f06d860c43f5f280207e5d880ad0d8323d824'


@app.route("/")
def index():
    conn = sqlite3.connect('car.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM periodic_service")
    res = cursor.fetchall();
    conn.close()
    
    histories = []

    for i in range (len(res)):
        sch =['n','engine_oil','engine_oil_filter','drain_plug_gasket','spark_plug','air_filter','radiator_coolant','brake_fluid','fuel_filter','transmission_oil_cvt','transmission_oil_filter','gasket_oil_pan','drain_plug','timing_belt_kit','fead_belt']
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
        lists = list
        for i in range(len(lists)):
            if lists[i] == 'engine_oil':
                lists[i] = 'Engine Oil'
            
            if lists[i] == 'engine_oil_filter':
                lists[i] = 'Engine Oil Filter'
 
            if lists[i] == 'drain_plug_gasket':
                lists[i] = 'Drain Plug Gasket'

            if lists[i] == 'spark_plug':
                lists[i] = 'Spark Plug'
 
            if lists[i] == 'air_filter':
                lists[i] = 'Air Filter'

            if lists[i] == 'radiator_coolant':
                lists[i] = 'Radiator Coolant'
            
            if lists[i] == 'brake_fluid':
                lists[i] = 'Brake Fluid'
 
            if lists[i] == 'fuel_filter':
                lists[i] = 'Fuel Filter'

            if lists[i] == 'transmission_oil_cvt':
                lists[i] = 'Transmission Oil CVT'
 
            if lists[i] == 'transmission_oil_filter':
                lists[i] = 'Transmission Oil Filter'

            if lists[i] == 'gasket_oil_pan':
                lists[i] = 'Gasket Oil Pan'
            
            if lists[i] == 'drain_plug':
                lists[i] = 'Drain Plug'
 
            if lists[i] == 'timing_belt_kit':
                lists[i] = 'Timing Belt Kit'

            if lists[i] == 'fead_belt':
                lists[i] = 'FEAD Belt'
 
        return render_template("confirmation.html", lists = lists )

    else: 
        return render_template("next_service.html", prechecked_service_list=prechecked_service_list)


@app.route("/confirmation", methods=["GET","POST"])
def confirmation():
    if request.method == "POST":
        conn = sqlite3.connect('car.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO periodic_service(engine_oil,engine_oil_filter,drain_plug_gasket,spark_plug,air_filter,radiator_coolant,brake_fluid,fuel_filter,transmission_oil_cvt,transmission_oil_filter,gasket_oil_pan,drain_plug,timing_belt_kit,fead_belt) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", session['confirmation_list'])
        conn.commit()
        conn.close()
        return render_template("next_service.html", prechecked_service_list=prechecked_service_list)
    else:
        return render_template("next_service.html", prechecked_service_list=prechecked_service_list)
    


@app.route("/delete_record", methods=["GET","POST"])
def delete_record():
    return render_template("delete_record.html")

@app.route("/about_me")
def about_me():
    return render_template("about_me.html")

@app.route("/index")
def redirect_index():
    return redirect("/")
