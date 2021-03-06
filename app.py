import firebase_admin
from firebase_admin import auth, firestore, storage, credentials
from flask import abort, jsonify, request, redirect
import json
import requests

#--------E N D  I M P O R T --------
app = flask.Flask(__name__)

cred = credentials.Certificate("tinderoken-firebase-adminsdk-dssce-43dc1f1794.json")
firebase_app firebase_admin.initialize_app(cred)
store = firestore.client()

@app.route('/login', methods=['POST'])
def login():
	data = requests.get_json(force=True)
	emailOfUser = data.get("email")
	uid = ""
	message = ""
	try:
		user = auth.get_user_by_email(emailOfUser)
		message = "Succesfully Got The new user"
		uid = user.uid
	except:
		messge = "User not there in firebase"

	return {"uid":uid, "message":message, "Response":200}
	return jsonify({"Response":200})



@app.route('/signup', methods=['POST'])
def signup():
	data = requests.get_json(force=True)
	emailOfUser = data.get("email")
	passwordOfUser = data.get("password")
	uid = ""
	message = ""
	try:
		user = auth.create_user(
			email=emailOfUser,
			email_verified=False,
			password=passwordOfUser)
		message = "Successfully created new user"
		uid = user.uid
	except:
		message = "User already there"

	return {"uid":uid, "message":message, "Response":200}
	return jsonify({"Response":200})



if __name__ == '__main__':
	app.run(host='0.0.0.0.', port=5001, debug=False)
