import web
import requests
import json
render = web.template.render("mvc/views/")

class Insert():

    def GET(self):
        try:
            return render.insert() # renderizando Log.html
        except Exception as e:
            return "Error " + str(e.args)
    def POST(self):
        try:
            form = web.input()
            name = form.nombre
            correo = form.email
            data_json ={
        
                'email':name,
                'name':correo
                
            }
            requests.post('https://fpyrebase-default-rtdb.firebaseio.com/personas.json',data=json.dumps(data_json))
            web.seeother('/Plist')
            #return render.plist()
            #web.seeother('/personas_list')
        except Exception as e:
            return "Error"+ str(e.args)