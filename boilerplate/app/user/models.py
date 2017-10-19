from flask_sqlalchemy import SQLAlchemy
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class regUser(db.Model):
	__tablename__ = 'users'
	#define here
	id = db.Column(db.Integer, autoincrement=True)
	email = db.Column(db.String, unique=True)
	password = db.Column(db.String(256))
	name = db.Column(db.String)
	roll = db.Column(db.Integer, primary_key=True)
	hostel = db.Column(db.String)
	room = db.Column(db.String)
	contact = db.Column(db.Integer)
	guardianAdd = db.Column(db.String)
	guardianCon = db.Column(db.Integer)
	status = db.Column(db.Integer)

	def __init__(self,name,roll,email,password,hostel,room,contact,guardianCon,guardianAdd,status):
		self.name = name
		self.roll = roll
		self.email = email
		self.password = generate_password_hash(password)
	#	self.password =password
	
		self.hostel = hostel
		self.room = room
		self.contact = contact
		self.guardianCon = guardianCon
		self.guardianAdd = guardianAdd
		self.status = status

	def check_password(self, password):
			return check_password_hash(self.password, password)

	def serialize(self):
		return {'name': self.name,
				'roll': self.roll,
				'email': self.email,
				'password': self.password,
				'hostel': self.hostel,
				'room': self.room,
				'contact': self.contact,
				'Guardian Address': self.guardianAdd,
				'Guardian Contact': self.guardianCon,
				'status': self.status}

	def __repr__(self):
		return "User<%d> %s" % (self.id, self.name)


class verUser(db.Model):
	__tablename__ = 'verified'
	#define here
	id = db.Column(db.Integer, autoincrement=True)
	email = db.Column(db.String, unique=True)
	password = db.Column(db.String(256))
	name = db.Column(db.String)
	roll = db.Column(db.Integer, primary_key=True)
	hostel = db.Column(db.String)
	room = db.Column(db.String)
	contact = db.Column(db.Integer)
	rating = db.Column(db.Integer, default=0)
	guardianAdd = db.Column(db.String)
	guardianCon = db.Column(db.Integer)
	status = db.Column(db.Integer)
	authenticated = db.Column(db.Boolean,default=False)


	def __init__(self,name,roll,email,password,hostel,room,contact,rating,guardianCon,guardianAdd,status,authenticated):
		self.name = name
		self.roll = roll
		self.email = email
	#	self.password = generate_password_hash(password)
		self.password = password
	
		self.hostel = hostel
		self.room = room
		self.contact = contact
		self.rating = rating
		self.guardianCon = guardianCon
		self.guardianAdd = guardianAdd
		self.status = status
		self.authenticated = authenticated

	def ver_check_password(self, password):
		if self.password == password:
			return True
		else:
			return False
		#	return check_password_hash(self.password, password)

	def check_password(self, password):
		return check_password_hash(self.password, password)

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
				'Guardian Contact': self.guardianCon,
				'status': self.status
				}

	def is_authenticated(self):
		"""Return True if the user is authenticated."""
		return self.authenticated

	def __repr__(self):
		return "%s" % ( self.name)

class Rating(db.Model):
	__tablename__ = 'ratings'
	#define here
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	#userRoll = db.Column(db.Integer, db.ForeignKey())
	#raterRoll = db.Column(db.Integer, db.ForeignKey())
	rating = db.Column(db.Integer, default=0)
	hash = db.Column(db.Integer, unique=True)

	def __init__(self,userRoll,raterRoll,rating):
		self.userRoll = userRoll
		self.raterRoll = raterRoll
		self.rating = rating
		self.hash = 10000000000*userRoll + raterRoll

	def serialize(self):
		return {'userRoll': self.userRoll,
				'raterRoll': self.raterRoll,
				'rating': self.rating,
				'hash': self.hash
				}

	def __repr__(self):
		return "%s" % ( self.rating)