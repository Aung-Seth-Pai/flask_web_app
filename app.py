'''
	Webapp for creating flexible schedule
	Google Calendar, Facebook Events, Gmail APIs
	Data Visualization on Task Accomplishments
'''

from flask import Flask, redirect, url_for, render_template, request, session
from form import RegisterForm, LoginForm
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from helper import login_required
# libs to hash password before storing them in db)

# create flask server
app = Flask(__name__)
app.config["SECRET_KEY"] = "9dfc64c5f1013516999739f20a4b13bc"
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# create database for users, todolist, time
# Users Table: id, username, hash and other user specific data

# set login_required decorator from cs50 
# Homepage
@app.route("/")
@app.route("/home")
@login_required
def index():
	# once decorated with login_required
	# it will check if current session["user_id"] is none
	# if none is true, login_required with redirect to /login
	# if not none, allow access to route
	user = session["user_id"]
	return render_template("index.html", title="Home", user = user)
	

# what happene when logged in user go to register route?
@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		# hash the password
		# save username and password in database
		# database contains (id) PRIMARY KEY AUTOINCREMENT
		# set session["user_id"] as saved id from database
		# redirect to home
		return redirect(url_for('index')) # register successful
	return render_template("register.html", title="register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	# clear any existing session >>> session.clear()
	# if request.method==POST validate the form submission
		# query database to check username and password hash
		# if fail
			# flash warning message, redirect to /login
		# if success
			# set session["user_id"] according to userdata in database
			# redirect to home page
	# if req.method==GET
		# render template(login.html)
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@gmail.com' and form.password.data == 'iamnumberone':
			# if validation success
			session['user_id'] = form.email.data
			#flash('Logged in successfully', 'success')
			return redirect(url_for('index'))
		else: # if fail
			#flash('403 Access Denied')
			return ('<h1>Access Denied</h1>')
	return render_template("login.html", title="login", form=form)

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

# enable server setup with (python filename.py) without (flask run)
if __name__ == '__main__':
	app.run(debug=True)