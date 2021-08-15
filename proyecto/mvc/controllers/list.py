import web
import pyrebase
import requests
from getpass import getpass
render = web.template.render("mvc/views/")
class List():

    def GET(self):
        try:
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
            
            db = firebase.database()
            result = db.child("personas").get()
            return render.list(result) # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)