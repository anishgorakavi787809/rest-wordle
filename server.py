
import imp
from flask import *
from flask_restful import *
import psycopg2
from wordgen import worldle_logic
connecter = psycopg2.connect(user="postgres",password="Checkred",host="127.0.0.1",database="wordle-rest")

cur = connecter.cursor()

app = Flask(__name__)
api = Api(app)
def logIn(username,password):
    cur.execute(f"select * from login where username='{username}' and password='{password}'")
    return cur.fetchone()

class TestLogin(Resource):
    def get(self):
        var = logIn(request.authorization["username"],request.authorization["password"])
        if var == None:
            return {"error":"wrong username or password"}
        else:
            return {"success":"Correct username and password"}

class SignUp(Resource):
    def post(self):
        uname = request.authorization["username"]
        pword = request.authorization["password"]
        cur.execute(f"insert into login(username,password) values('{uname}','{pword}')")
        return {"success":"Signed u up!"}

api.add_resource(TestLogin,"/test_login")
api.add_resource(SignUp,"/signup")
app.run(debug=True)