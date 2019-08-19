'''
	Webapp for creating flexible schedule
	Google Calendar, Facebook Events, Gmail APIs
	Data Visualization on Task Accomplishments
'''

from flask import Flask, redirect, url_for, render_template, request
from form import RegisterForm, LoginForm
import sqlite3

# create flask server
app = Flask(__name__)
app.config["SECRET_KEY"] = "9dfc64c5f1013516999739f20a4b13bc"
app.config["TEMPLATES_AUTO_RELOAD"] = True

# create database for users, todolist, time

# Homepage
@app.route("/")
@app.route("/home")
def index():
	return render_template("index.html", title="Home")

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		return redirect(url_for('index')) # register successful
	return render_template("register.html", title="register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		return redirect(url_for('index')) # login successful
	return render_template("login.html", title="login", form=form)

# enable server setup with (python filename.py) without (flask run)
if __name__ == '__main__':
	app.run(debug=True)