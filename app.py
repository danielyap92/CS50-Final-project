import os
import sqlite3
from flask import Flask, flash, redirect, render_template, request

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

@app.route("/next_service")
def next_service():
    return render_template("next_service.html")

@app.route("/delete_record")
def delete_record():
    return render_template("delete_record.html")

@app.route("/about_me")
def about_me():
    return render_template("about_me.html")

@app.route("/index")
def redirect_index():
    return redirect("/")
