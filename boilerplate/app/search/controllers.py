from flask import Blueprint, request, render_template, \
				  flash, g, session, redirect, url_for,jsonify,make_response
from app import db
from app.search.models import Search
from app.user.models import verUser
from flask_cors import CORS

mod_search = Blueprint('search', __name__)


@mod_search.route('/search', methods=['POST'])
def search():
	opject = {'students' : []}
	inp = request.form['fill']
	#inp = inp.lower()
	p = []
	l = len(inp)
	user_list = verUser.query.all()
	for i in user_list:
#		stri=str(i.name[:l])
#	if(stri == inp)
		p.append(i.name)
		opject['students'].append(i.serialise())
	return jsonify(opject)
