# Import flask and template operators
from flask import Flask, render_template
from flask import *
# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404



# Import a module / component using its blueprint handler variable (mod_auth)
from app.admin.controllers import mod_admin
from app.user.controllers import mod_user
from app.report.controllers import mod_report
from app.search.controllers import mod_search
from app.update.controllers import mod_update



# Register blueprint(s)
app.register_blueprint(mod_admin)
app.register_blueprint(mod_user)
app.register_blueprint(mod_update)
app.register_blueprint(mod_search)
app.register_blueprint(mod_report)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
