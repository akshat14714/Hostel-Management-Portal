from flask import Blueprint, request, render_template, \
				  flash, g, session, redirect, url_for,jsonify,make_response
from app import db
from app.report.models import Report
#from app.report.models import Comments
from app.user.models import verUser
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS

mod_report = Blueprint('report', __name__)
CORS(mod_report)

global a
a = ''

@mod_report.route('/addComplaint', methods=['GET', 'POST'])
def addComplaint():
		if 'roll' and 'email' not in session:
				return redirect('/login')

		if request.method == 'GET':
				return render_template('addComplaint.html')
		else:
				try:
					if 'roll' in session:
							roll = session['roll']
					else:
							roll = session['email']
					title = request.form['About']
					complaint = request.form['comp']
				except KeyError as e:
					return jsonify(success=False, message="%s not sent in request" % e.args), 400

				user = verUser.query.filter(verUser.roll == roll).first()
				print(user)

				if user is None:
						return jsonify(success=False, message="Invalid Credentials"), 400

				done = Report(roll, title, complaint, )
				print(done)
				db.session.add(done)
				
				try:
					db.session.commit()
				except IntegrityError as e:
					return jsonify(success=False, message="Complaint already exists")

				return jsonify(success=True, message="Your complaint has been recorded")

@mod_report.route('/getAllComplaints', methods=['GET'])
def get_all():
		opject = {'complaints' : []}
		comp = Report.query.all()
		for var in comp:
			opject['complaints'].append(var.serialize())
		return jsonify(opject)

@mod_report.route('/addComment', methods=['GET', 'POST'])
def comment():
	global a
	a = request.url
	reports = Report.query.all()
	
	if request.method == 'GET':
		return render_template('addComment.html', reports=reports)
	else:
		try:
			#if 'roll' in session:
			#		roll = session['roll']
			#else:
			#		roll = session['email']
			title = request.form['title']
		except:
			return jsonify(success=False, message="%s not sent in the request" % e.args), 400
		
		comp = Report.query.filter(Report.title == title).first()
		rid = comp.id

		comment = request.form['comment']
		comp.comment = comment
		db.session.commit()

		return jsonify(success=True, message="Your comment has been recorded")
