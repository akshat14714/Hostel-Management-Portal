from flask import Blueprint, request, render_template, \
				  flash, g, session, redirect, url_for,jsonify,make_response
from app import db
from app.update.models import Update
from app.user.models import verUser
#from flask_cors import CORS

mod_update = Blueprint('update', __name__)

@mod_update.route('/update', methods=['POST','GET'])
def update_user():
	if 'email' in session and 'roll' not in session:
		return redirect('/login')
	if 'roll' in session:
		roll = session['roll']
		#return roll
		if request.method == 'GET':
		   return render_template('updateuser.html')
		else:
			try:
			   #email = request.form['email']
				hostel = request.form['hostel']
				room = request.form['room']
				contact = request.form['contact']
				guardianAdd = request.form['guardianAdd']
				guardianCon = request.form['guardianCon']

			except KeyError as e:
				return jsonify(success=False, message="%s not sent in the request" % e.args), 400

	#if '@' not in email:
	#    return jsonify(success=False, message="Please enter a valid email"), 400

			u = verUser.query.filter(verUser.roll==roll).first()
			#print(u)
			if hostel!='':
				u.hostel = hostel
			if room!='':
				u.room = room
			if contact!='':
				u.contact = contact
			if guardianCon!='':
				u.guardianCon = guardianCon
			if guardianAdd!='':
				u.guardianAdd = guardianAdd
			#db.session.add(u)
			db.session.commit()

		return redirect('/?roll='+roll)
	else:
		return redirect('/login')