from flask_sqlalchemy import SQLAlchemy
from app import db

class Update(db.Model):
	__tablename__ = 'update'

	#define here
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	hostel = db.Column(db.String)
	room = db.Column(db.String,unique=True)
	contact = db.Column(db.Integer,unique=True)
	guardianAdd = db.Column(db.String)
	guardianCon = db.Column(db.String)

	def __init__(self,hostel,room,contact,guardianCon,guardianAdd):
		self.hostel = hostel
		self.room = room
		self.contact = contact
		self.guardianAdd = guardianAdd
		self.guardianCon = guardianCon

	def serialize(self):
		return {'hostel': self.hostel,
				'room': self.room,
				'contact': self.contact,
				'Guardian Address': self.guardianAdd,
				'Guardian Contact': self.guardiancontact}

	def __repr__(self):
		return "User<%d> %s" % (self.id, self.name)
