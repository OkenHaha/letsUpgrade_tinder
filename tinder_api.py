import firebase_admin
from firebase_admin import auth, firestore, storage, credentials
#--------E N D  I M P O R T --------

#D A T A B A S E
cred = credentials.Certificate("tinderoken-firebase-adminsdk-dssce-43dc1f1794.json")
firebase_app firebase_admin.initialize_app(cred)
store = firestore.client()

def login(emailOfUser, passwordOfUser):
	uid = ""
	message = ""
	try:
		user = auth.get_user_by_email(emailOfUser)
		message = "Succesfully created new user"
		uid = user.uid
	except:
		messge = "User not there in firebase"

	return {"uid":uid, "message":message}

login("name@domain.com", "123456")

#----------- E N D   L O G I N ------------------

def signUP(emailOfUser, passwordOfUser):
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

	return {"uid":uid, "message":message}

signUp("oken@oken.com", "oken1234)


#---------E N D   S I G N U P------------------------

def updateUserData(dit):
	dit_user_details= {}
	dit_user_details['name'] = dit.get["name"]
	dit_user_details['email'] = dit.get["email"]
	dit_user_details['number'] = dit.get["number"]
	dit_user_details['image'] = dit.get["image"]
	dit_user_details['desp'] = dit.get["desp"]
	dit_user_details['dob'] = dit.get["dob"]
	dit_user_details['gender'] = dit.get["gender"]
	dit_user_details['passion'] = dit.get["passion"]
	dit_user_details['job'] = dit.get["job"]
	dit_user_details['company'] = dit.get["company"]
	dit_user_details['location'] = dit["location"]
	dit_user_details['createdAt'] = firestore.SERVER_TIMESTAMP
	store.collection("users").document(uid).set(dit_user_details) #to store data inside firebase

	dit = {}
	dit['name'] = "Oken"
	 dit['email'] = "sdfgfg@dfsgf.com"
	dit['number'] = "234234"
	dit['image'] = "imageURL"
	dit['desp'] = "single"
	dit['location'] = {"coordinate":{"lat":, "lng":},
						"city":"Mumbai",
						"state":"Maha",
						"country":"India"}
	dit['dob'] = "12/12/1999"
	dit['gender'] = "male"
	dit['passion'] = "Coding"
	dit['job'] = "student"
	dit['company'] = "none"

	updateUserData("uid", dit)

	#------------E N D    P R O F I L E----------------------

def getFeed(country):
	docs = store.collection("users").stream()
	dit = {}
	for i in docs:
		if doc.to_dict().get("location").get("country") == country:
			dit[doc.id]= doc.to_dict()

	return dit


allProfiles = getFeed("india")
allProfiles

#--------------E N D   O F  F E E D -----------

def swipeFun(uidA, uidB, isA_Yes, isB_Yes):
	dit = {}
	dit['UID_A'] = uidA
	dit['UID_B'] = uidB
	dit["isUserA_Yes"] = isA_Yes
	dit['isUserB_Yes'] = isB_Yes
	dit['SawOnce'] = firstTime
	dit['createdAt'] = firestore.SERVER_TIMESTAMP

	store.collection("swipes").add(dit)

uidA = "uid"
uidB = "uid"
isA_Yes = True
isB_Yes = False
firstTime = False
swipeFun(uidA, uidB, isA_Yes, isB_Yes, firstTime)

#---------E N D   S W I P E -----------

def getMatchFun(uid):
	docs = store.collection("swipes").stream()

	ditSwipes = {}
	for doc in docs:
		if (doc.to_dict().get("UID_A") == uid or doc.to_dict().get("UID_B") == uid) and (doc.to+dict().get("isUserA_Yes") == True and doc.to_dict().get().get("isUserB_Yes") == True):
			ditSwipes[doc.id] = doc.to_dict()


	return ditSwipes
