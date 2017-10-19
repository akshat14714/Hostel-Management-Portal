from flask_sqlalchemy import SQLAlchemy
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Admin(db.Model):
	__tablename__ = 'admin'
	#define here
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String)
	email = db.Column(db.String, unique=True)
	password = db.Column(db.String)

	def __init__(self,name,email,password):
		self.name = name
		self.password = generate_password_hash(password)
		self.email = email

	def check_password(self, password):
			return check_password_hash(self.password, password)

	def serialize(self):
		return {'name': self.name,
				'password': self.password,
				'email': self.email}

	def __repr__(self):
		return "User<%d> %s" % (self.id, self.name)

class SearchTable(db.Model):
	__tablename__ = 'Search'
	#define here
	id_s = db.Column(db.Integer, autoincrement=True)
	email = db.Column(db.String, unique=True)
#	password = db.Column(db.String(256))
	name = db.Column(db.String)
	roll = db.Column(db.Integer, primary_key=True)
	hostel = db.Column(db.String)
	room = db.Column(db.String, unique=True)
	contact = db.Column(db.Integer)
	rating = db.Column(db.Integer)
	guardianAdd = db.Column(db.String)
	guardianCon = db.Column(db.Integer)
#	status = db.Column(db.Integer)

	def __init__(self,name,roll,email,hostel,room,contact,rating,guardianCon,guardianAdd):
		self.name = name
		self.roll = roll
		self.email = email
		self.hostel = hostel
		self.room = room
		self.contact = contact
		self.rating = rating
		self.guardianCon = guardianCon
		self.guardianAdd = guardianAdd

	def serialize(self):
		return {'name': self.name,
				'roll': self.roll,
				'email': self.email,
				'password': self.password,
				'hostel': self.hostel,
				'room': self.room,
				'contact': self.contact,
				'rating': self.rating,
				'Guardian Address': self.guardianAdd,
				'Guardian Contact': self.guardianCon}
#				'status': self.status}

	def __repr__(self):
		return "User %s" % (self.name)


class VerifyTable(db.Model):
	__tablename__ = 'verify'
	#define here
#	id_s = db.Column(db.Integer, autoincrement=True)
	email = db.Column(db.String, unique=True)
#	password = db.Column(db.String(256))
	name = db.Column(db.String)
	roll = db.Column(db.Integer, primary_key=True)
	hostel = db.Column(db.String)
	room = db.Column(db.String, unique=True)
	contact = db.Column(db.Integer)
	guardianAdd = db.Column(db.String)
	guardianCon = db.Column(db.Integer)
#	status = db.Column(db.Integer)

	def __init__(self,name,roll,email,hostel,room,contact,guardianCon,guardianAdd):
		self.name = name
		self.roll = roll
		self.email = email
#		self.password = generate_password_hash(password)
		self.hostel = hostel
		self.room = room
		self.contact = contact
		self.guardianCon = guardianCon
		self.guardianAdd = guardianAdd

	def serialize(self):
		return {'name': self.name,
				'roll': self.roll,
				'email': self.email,
				'hostel': self.hostel,
				'room': self.room,
				'contact': self.contact,
				'Guardian Address': self.guardianAdd,
				'Guardian Contact': self.guardianCon}
				#'status': self.status}

	def __repr__(self):
		return "User %s" % (self.name)