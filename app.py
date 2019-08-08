'''
	Webapp for creating flexible schedule
	Google Calendar, Facebook Events, Gmail APIs
	Data Analysis on Task Accomplishments
'''

from flask import Flask, redirect, url_for, render_template
from flask_wtf import FlaskForm
import sqlite3

# create flask server
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# create database for users, todolist, time

# Homepage
@app.route("/")
@app.route("/home")
def index():
	return render_template("index.html", title="Home")

# enable server setup with (python filename.py) without (flask run)
if __name__ == '__main__':
	app.run(debug=True)