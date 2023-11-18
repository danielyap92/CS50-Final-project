import sqlite3
from flask import Flask, flash, redirect, render_template, request

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")
