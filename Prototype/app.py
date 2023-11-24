# import os
import sqlite3
from flask import Flask, flash, redirect, render_template, request
from sch import last_number_of_service, current_number_service, prechecked_service_list


app = Flask(__name__)



@app.route("/")
def index():
    conn = sqlite3.connect('car.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM periodic_service")
    res = cursor.fetchall();

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
    
    conn.close()

@app.route("/next_service", methods=["GET", "POST"])
def next_service():
    if request.method == "POST":
        list = request.form.getlist("service_checkbox")
        # below may migrate to confirmation page
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
        # above may migrate to confirmation page
        return render_template("next_service.html", prechecked_service_list=prechecked_service_list) 
    #     if request.form.get("engine_oil"):
    #         print("U checked engine oil")
    #         return render_template("next_service.html", servicedict=servicedict)
    #     else:
    #         print("U do not checked engine oil")
    #         return render_template("next_service.html", servicedict=servicedict)
    else: 
        return render_template("next_service.html", prechecked_service_list=prechecked_service_list)

@app.route("/delete_record")
def delete_record():
    return render_template("delete_record.html")

@app.route("/about_me")
def about_me():
    return render_template("about_me.html")

@app.route("/index")
def redirect_index():
    return redirect("/")
