from flask import *
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import func
from app import db
from .models import regUser
from .models import verUser
from app.report.models import Report
from werkzeug.security import generate_password_hash, check_password_hash

from flask_cors import CORS

mod_user = Blueprint('user', __name__)
CORS(mod_user)


global a
a=''

@mod_user.route('/',methods=['GET'])
def func():
	if 'roll' not in session and 'email' not in session:
		return redirect('/login')		
	return render_template('index.html')

@mod_user.route('/logout', methods=['GET'])
def logout():
	if 'roll' in session:
		session.pop('roll')
	elif 'email' in session:
		session.pop('email')
	return redirect('/login')
	#return jsonify(success=True, message="Logout Successful")

@mod_user.route('/registerUser', methods=['POST' ,'GET'])
def create_User():
	if 'email' in session:
		session.pop('email')
	if 'roll' in session:
		session.pop('roll')
	if request.method == 'GET':
		global a
		a=request.url	
		return render_template('adduser.html')
	else:
		try:
			name = (request.form['name']).lower()
			email = request.form['email']
			password = request.form['password']		
			roll = request.form['roll']
			hostel = request.form['hostel']
			room = request.form['room']
			contact = request.form['contact']
			guardianAdd = request.form['guardianAdd']
			guardianCon = request.form['guardianCon']
		except KeyError as e:
			return jsonify(success=False, message="%s not sent in the request" % e.args), 400
		
		if name=='' or email=='' or password=='' or roll=='' or hostel=='' or room=='' or contact=='' or guardianCon=='' or guardianAdd=='': 
			return make_response('Please fill the entries', 400 , None)
			#	return jsonify(success=False, message="Invalid Credentials"), 400

		if '@' not in email:
			return make_response('Please enter a valid email', 400 , None)
			#return jsonify(success=False, message="Please enter a valid email"), 400
	
		for i in verUser.query.all():
			if i.email == email:
				return make_response('email already verified', 400 , None)
				#return jsonify(success=False,message="already verified")
	
		user = regUser(name,roll,email,password,hostel,room,contact,guardianCon,guardianAdd,1)
#		user.status = 1
	#	print(user)
		db.session.add(user)

		try:
			db.session.commit()
		except IntegrityError as e:
		#	db.session.rollback()
			return jsonify(success=False, message="This email already exists"), 400

		return jsonify(success=True)

@mod_user.route('/getAllRegUser', methods=['GET'])
def get_all_reg():
		global a
		a=request.url
		if 'email' not in session:
			 return redirect('/login')
	
		opject = {'users' : []}
		user = regUser.query.all()
		for var in user:
			opject['users'].append(var.serialize())
		return jsonify(opject)

@mod_user.route('/login', methods=['POST' ,'GET'])
def login():
	#a=request.url
		
	global a	
	if request.method == 'GET':
		if 'roll' in session:
			#return session['roll']
			session.pop('roll')
		if 'email' in session:
			session.pop('email')
		#return  a
		return render_template('login1.html')
	else:
		try:
			roll = request.form['roll']
			password = request.form['password']
		except KeyError as e:
			return jsonify(success=False, message="%s not sent in the request" % e.args), 400

		
		user = verUser.query.filter(verUser.roll == request.form['roll']).first()
		#return jsonify(user.ver_check_password('k'))
		if user is None or not user.check_password(password):
			return make_response('Invalid Password or RollNo', 400 , None)
			#return redirect('/')
			#	return jsonify(success=False, message="Invalid Credentials"), 400
		user.authenticated = True

		session['roll'] = roll
		if not a:
			return redirect("/")
		return redirect(a)
		#return redirect('/usersearch')
		#return jsonify(success=True, message="Login Successfully",user = user.serialize())

@mod_user.route('/usersearch', methods=['GET','POST'])
#@requires_auth_user
def search():
	global a
	a=request.url
	if 'roll' not in session:
		return redirect('/login')
	
	if request.method == 'GET':
		return render_template('usersearch.html')
	else:
		try:
			init = (request.form['enter']).lower()
		except KeyError as e:
			return jsonify(success=False, message="%s not sent in the request" % e.args), 400

		users = verUser.query.all()
		opject = {'results' : []}
		for i in users:
			s=[]
			str1 = i.name
			if(str1.find(init)!=-1):
				s.append(i.name)
				s.append(i.roll)
				s.append(i.email)
				s.append(i.hostel)
				s.append(i.room) 
				s.append(i.rating)	
			#	contact = i.contact
				#guardianCon = i.guardianCon
				#guardianAdd = i.guardianAdd
				#s = (name,roll,email,hostel,room)
				#print(s)
				#db.session.add(s)
				#if i.status == 2:
				opject['results'].append(s)

#			return render_template('results.html' , users = opject)	
				db.session.commit()
#				return make_response('success: k', 200, None)
		   
#                return make_response('error: ectly', 400, None)
#				return make_response('success : found' , 200, None)			
#		return None
	return	jsonify(opject)

#<<<<<<< HEAD
#'''@mod_user.route("/<roll>", methods=['GET'])
#=======

@mod_user.route("/roll", methods=['GET'])
#>>>>>>> 983c210d0ea783465b655b31f4c61c6027b9a9c2
def search_roll():
	global a
	a=request.url
	roll = request.args.get('roll')
	print(a)
	print(roll)
	if 'roll' not in session and 'email' not in session:
		return redirect('/login')
	
	user = verUser.query.filter(verUser.roll == roll).first()
	return jsonify(user.serialize())
#'''

@mod_user.route("/rate", methods=['GET', 'POST'])
def rate():
	global a
	a = request.url
	if 'roll' not in session:
		return redirect("/login")
	
	users = verUser.query.all()

	if request.method == 'GET':
		return render_template("rateUser.html", users=users)
	else:
		try:
			roll = request.form['roll']
		except:
			return jsonify(success=False, message="%s not sent in the request" % e.args), 400
		
		user = verUser.query.filter(verUser.roll == roll).first()

		response = request.form['option']
		prev = user.rating

		user.rating = func.add(prev, response)

		db.session.commit()

		return jsonify(success=True, message="You have rated the user")