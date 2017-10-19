from flask_sqlalchemy import SQLAlchemy
from app import db
from app.user.models import verUser

class Report(db.Model):
	__tablename__ = 'reports'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	roll = db.Column(db.Integer)
	#password = db.Column(db.String)
	title = db.Column(db.String)
	quer = db.Column(db.String(2000))
	#comments = db.relationship('Comments', backref='query', lazy='dynamic')
	#comment = db.Column(db.String)
	#status = db.Column(db.Integer, default=0)
	#user_roll = db.Column(db.Integer)#, db.ForeignKey('user.roll'))

	def __init__(self, roll, title, quer):
		self.roll = roll
		#self.password = password
		self.title = title
		self.quer = quer
		#self.comment = 
		#self.user_roll = user_roll

	def serialize(self):
		return {
				'id': self.id,
				'roll no': self.roll,
				'title': self.title,
				'query': self.quer,
				'comments': comments
				#'status': self.status,
			}

	def __repr__(self):
		return "%s" % (self.title)
'''
class Comments(db.Model):
	__tablename__= 'comments'
	
	#id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	rid = db.Column(db.Integer, db.ForeignKey('reports.id'))
	#name = db.Column(db.String, unique=True)
	comment = db.Column(db.String)

	def __init__(self, comment):
		#self.name = name
		self.comment = comment

	def serialize(self):
		return {
			#'name': self.name,
			'comment': self.comment
		}
	
	def __repr__(self):
		return"%s" % (self.comment)'''