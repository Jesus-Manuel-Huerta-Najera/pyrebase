import web
import pyrebase
render = web.template.render("mvc/views/")
class Index():

    def GET(self):
        try:
            result=""
            return render.index(result) # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)
    def POST(self):
        try:
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
            form = web.input()
            #print(forms)
            mail = form.mail
            passw = form.passw
            user = auth.sign_in_with_email_and_password(mail,passw)
            if user!="":
                result="Cuenta si registrada"
                return render.index(result)
                #web.seeother('/Plist')
            
            #model_alumnos.update(matricula,nombre,Ap,Am,date,gen,estado,ids)
            #web.seeother('/Plist')
        except Exception as e:
            result="Cuenta no registrada"
            return render.index(result)