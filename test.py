import pyrebase
import requests
import json
from getpass import getpass

firebaseConfig  = {
    "apiKey": "AIzaSyCgy1xQYP-28ufvMbaMog18VshMrG_pGmk",
    "authDomain": "pyrebase-d4022.firebaseapp.com",
    "databaseURL": "https://fpyrebase-default-rtdb.firebaseio.com/",
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
try:
    print("buena onda ---------------------")
    db = firebase.database()
    all_users = db.child("personas").get()
    for user in all_users.each():
        print(user.key()) # Morty
        print(user.val()) # {name": "Mortimer 'Morty' Smith"}
        print(user.val()['name']) # {name": "Mortimer 'Morty' Smith"}
except Exception as e:
    print(e.args[0])  

try:
    data_json={
        
        'email':"bigameroso@gmail.com",
        'name':"Jesus Manuel"
        
    }
    result= requests.post('https://fpyrebase-default-rtdb.firebaseio.com/personas.json',data=json.dumps(data_json))
    print (result)
except Exception as error:
    print(error.args[0])

