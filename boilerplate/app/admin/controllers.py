from flask import *
from app import db
from app.admin.models import Admin
from app.admin.models import SearchTable
from app.admin.models import VerifyTable
from app.user.models import verUser
from app.user.models import regUser
from flask_cors import CORS

mod_admin = Blueprint('admin', __name__)
CORS(mod_admin)

#@mod_admin.route('/getSearch' , methods=['GET', 'POST'])
#def result():
global a
a=''

@mod_admin.route('/addAdmin', methods=['GET','POST'])
def create_admin():
	klm = 'lodalassan'
	global a
	a=request.url
	if request.method == 'GET':
		return render_template('addadmin.html')
	else:
		try:
			name = (request.form['name']).lower()
			email = request.form['email']
			password = request.form['password']
			auth = request.form['auth']

		except KeyError as e:
			return jsonify(success=False, message="%s not sent in the request" % e.args), 400
		
		if name=='' or email=='' or password=='' or auth=='':
			return jsonify(success=False, message="Invalid Credentials"), 400

		if '@' not in email:
			return jsonify(success=False, message="Please enter a valid email"), 400

		if  auth != klm :
			return jsonify(success=False, message="Authentication Req"), 400
		
		admin = Admin(name,email,password)
		db.session.add(admin)
		
		try:	
			db.session.commit()
		except IntegrityError as e:
			return jsonify(success=False, message="This email already exists"), 400
	
		return jsonify(success = True)


@mod_admin.route('/getAllRegUser', methods=['GET'])

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


@mod_admin.route('/getAllUser', methods=['GET'])
#@requires_auth_user
def get_all_user():
	global a
	a=request.url
	#return a
	if 'roll' in session:
		session.pop('roll')
	if 'email' not in session:
		return redirect('/login')
	#return session['email']
	opject = {'users' : []}
	user = verUser.query.all()
	for var in user:
		opject['users'].append(var.serialize())
	
	return jsonify(opject)

@mod_admin.route('/getAllAdmin', methods=['GET'])
def get_all():
		global a
		a=request.url
		if 'email' not in session:
			return redirect('/login')
	
		opject = {'admin' : []}
		admin = Admin.query.all()
		for var in admin:
			opject['admin'].append(var.serialize())
		return jsonify(opject) 

@mod_admin.route('/adSearch', methods=['GET','POST'])
def search():
	global a
	a=request.url
	if 'email' not in session:
		return redirect('/login')
	
	if request.method == 'GET':
		return render_template('adminsearch.html')
	else:
		try:
			init = (request.form['enter']).lower()
		except KeyError as e:
			return jsonify(success=False, message="%s not sent in the request" % e.args), 400

		users = verUser.query.all()
		opject = {'results' : []}
		arr= []
		for i in users:
			str1 = i.name
			if(str1.find(init)!=-1):
			
				#opjec['results'].append(i.serialize())
				arr.append(i.serialize())
				db.session.commit()

	return	jsonify(arr)
#=======
	return render_template('results.html' , users = arr)
	#return	jsonify(opject)

@mod_admin.route('/updateStatus', methods=['GET', 'POST'])
def status():
	#print(Admin.query.all())
	global a
	a=request.url
	if 'email' not in session:
		return redirect('/login')
	
	users = regUser.query.filter(regUser.status == 1)	
	if request.method == 'GET':
		print(users)
		return render_template('updatestatus.html' , users=users)
	else:
		try:
			email = request.form['email']
		except:
			return jsonify(success=False, message="%s not sent in the request" % e.args), 400

		user = regUser.query.filter(regUser.email == email).first()
#		for user in users:

		checked = request.form['option']
		if checked == 'verified':
			user.status = 2
		elif checked == 'rejected':
			user.status = 3
		else:
			user.status = 1
		if user.status == 2:
#    		verified.status = 2
			verified = verUser(user.name,user.roll,user.email,user.password,user.hostel,user.room,user.contact,0,user.guardianCon,user.guardianAdd,user.status,False)
			db.session.add(verified)
			db.session.commit()
		db.session.delete(user)
		db.session.commit()

		return jsonify(success=True, message="User status updated")

@mod_admin.route('/adlogin', methods=['POST' ,'GET'])
def login():
	if request.method == 'GET':
		if 'email' in session:
			session.pop('email')
		if 'roll' in session:
			session.pop('roll')
		return render_template('adlogin.html')
	else:
		try:
			email = request.form['email']
			password = request.form['password']
			print(email)
		except KeyError as e:
			return jsonify(success=False, message="%s not sent in the request" % e.args), 400

		#if '@' not in email:
		#		return jsonify(success=False, message="Please enter a valid email"), 400
		
		ad = Admin.query.filter(Admin.email == request.form['email']).first()
		#return jsonify(ad.check_password('k'))
		if ad is None or not ad.check_password(password):
				return jsonify(success=False, message="Invalid Credentials"), 400

		session['email'] = email
		if not a:
			return redirect("/adSearch")
		return redirect(a)
		#return jsonify(success=True, message="Login Successfully")
