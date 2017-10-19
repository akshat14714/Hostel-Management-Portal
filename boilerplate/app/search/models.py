from flask_sqlalchemy import SQLAlchemy
from app import db

class Search(db.Model):
	__tablename__ = 'search'

	#define here
	id = db.Column(db.Integer,primary_key=True, autoincrement=True)
	name = db.Column(db.String)

	def __init__(self,name):
		self.name = name

	def serialize(self):
		return {'name':name}
