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
        dic = dict(zip(sch,res[i]))
        histories.append(dic)

    return render_template("index.html", histories=histories)
    
    conn.close()
