from flask import redirect, url_for, render_template, request, session, flash
from app import app
from werkzeug.security import generate_password_hash, check_password_hash
from app.helper import login_required
from app.forms import RegisterForm, LoginForm, ContentForm

# create database for users, todolist, time
# Users Table: id, username, hash and other user specific data
userdata = []

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
	form = ContentForm()
	user = session["user_id"]
	return render_template("index.html", title="Home", user = user,
							password = userdata[0]['password'],
							hashed_pwd = userdata[0]['hashed_pwd'], form=form)

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
		flash("Account successfully created!", "success")
		return redirect(url_for('index')) # register successful
	return render_template("register.html", title="register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		# query database to check username and password hash
		if form.email.data == 'admin@gmail.com' and form.password.data == 'iamnumberone':
			# if validation success
			# set session["user_id"] according to userdata in database
			hashed_pwd = generate_password_hash(form.password.data)
			userdata.append({'username': f'{form.email.data}',
						 'password': f'{form.password.data}',
						 'hashed_pwd': f'{hashed_pwd}'})

			session['user_id'] = form.email.data
			flash('Logged in successfully', 'success')
		#----End test----
			return redirect(url_for('index'))
		else: # if fail
			flash("Access Denied", "danger")
	return render_template("login.html", title="login", form=form)

@app.route("/logout")
def logout():
    """Log user out"""
    userdata.clear()
    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect(url_for('index'))