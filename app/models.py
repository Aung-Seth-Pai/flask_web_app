from datetime import datetime
from app import db


class User(db.Model):
	# index help db searches faster
	user_id	= db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True, nullable=False)
	email	= db.Column(db.String(64), index=True, unique=True, nullable=False)
	pwd_hash = db.Column(db.String(128), nullable=False)

	# tell python how to print objects of this(self) class
	def __repr__(self):
		return '<User {}>'.format(self.username)