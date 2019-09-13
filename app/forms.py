from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.fields.html5 import DateTimeLocalField

class RegisterForm(FlaskForm):
	username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()] )
	password = PasswordField('Password', validators=[DataRequired()] )
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class ContentForm(FlaskForm):
	deadline = DateTimeLocalField('Set Course Deadline', format='%m/%d/%y', validators=[DataRequired()])
	submit = SubmitField('Submit')