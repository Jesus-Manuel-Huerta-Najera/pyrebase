import pyrebase
from getpass import getpass

firebaseConfig  = {
    "apiKey": "AIzaSyCgy1xQYP-28ufvMbaMog18VshMrG_pGmk",
    "authDomain": "pyrebase-d4022.firebaseapp.com",
     "databaseURL": "https://pyrebase-d4022-default-rtdb.firebaseio.com",
    "projectId": "pyrebase-d4022",
    "storageBucket": "pyrebase-d4022.appspot.com",
    "messagingSenderId": "661495265135",
    "appId": "1:661495265135:web:ce695dc5c278c401541a9a",
    "measurementId": "G-1QYQ80JGLX"
}

firebase = pyrebase.initialize_app(firebaseConfig )

auth = firebase.auth()

email = "test@gmail.com"
password = 123456

user = auth.sign_in_with_email_and_password(email,password)
if user!="":
    print("buena")
    print(user['idToken'])
else:
    print("error")
   

