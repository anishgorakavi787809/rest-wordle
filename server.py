
 
from flask import *
from flask_restful import *
import psycopg2
from wordgen import worldle_logic
from  werkzeug.security import *
connecter = psycopg2.connect(user="postgres",password="Checkred",host="127.0.0.1",database="wordle-rest")

cur = connecter.cursor()

app = Flask(__name__)
api = Api(app)
logic = worldle_logic("words.json")
def logIn(username,password):
    cur.execute(f"select password from login where username='{username}'")
    try:
        vary = check_password_hash(cur.fetchone()[0],password)
        return vary
    except:
        return cur.fetchone()

class TestLogin(Resource):
    def get(self):
        var = logIn(request.authorization["username"],request.authorization["password"])
        print(var)
        if not var :
            return {"error":"wrong username or password"}
        else:
            return {"success":"Correct username and password"}

class SignUp(Resource):
    def post(self):
        uname = request.authorization["username"]
        pword = request.authorization["password"]
        cur.execute(f"insert into login(username,password) values('{uname}','{generate_password_hash(pword)}')")
        connecter.commit()
        cur.execute("""insert into wordle (username,guesses,guess1,guess2,guess3,guess4,guess5) values('%s',0,'{"null":"nullman"}','{"null":"nullman"}','{"null":"nullman"}','{"null":"nullman"}','{"null":"nullman"}')""" % request.authorization["username"])
        connecter.commit()
        return {"success":"Signed u up!"}

class Guess(Resource):
    def get(self,word):
        var = logIn(request.authorization["username"],request.authorization["password"])
        if not var :
            return {"error":"wrong username or password"}
        else:
            uname = request.authorization["username"]
            cur.execute(f"select guesses from wordle where username='{uname}'")
            num = cur.fetchone()[0]
            
            if num == 0:
                    word_dex = logic.letter_find(word)
                    try:
                        word_dex["error"]
                        return word_dex
                    except:
                        word_dex = str(word_dex).replace("'",'"')
                        if word == logic.get_word_day():
                            print(word_dex)
                            cur.execute(f"update wordle set guess5 = '{word_dex}' where username='{uname}'")
                            connecter.commit()
                            cur.execute(f"update wordle set guesses = 5 where username = '{uname}'")
                            connecter.commit()
                            return {"success":f"You guessed the correct word which is {logic.get_word_day()}"}
                        print(word_dex)
                        cur.execute(f"""update wordle set guess1 = '{word_dex}' where username='{uname}'""")
                        connecter.commit()
                        cur.execute(f"update wordle set guesses = 1 where username = '{uname}'")
                        connecter.commit()
                        return {"result":logic.letter_find(word), "attempts":"1/5"}
            if num ==  1:
                    word_dex = logic.letter_find(word)
                    try:
                        word_dex["error"]
                        return word_dex
                    except:
                        word_dex = str(word_dex).replace("'",'"')
                        if word == logic.get_word_day():
                            print(word_dex)
                            cur.execute(f"update wordle set guess5 = '{word_dex}' where username='{uname}'")
                            connecter.commit()
                            cur.execute(f"update wordle set guesses = 5 where username = '{uname}'")
                            connecter.commit()
                            return {"success":f"You guessed the correct word which is {logic.get_word_day()}"}

                        print(word_dex)
                        cur.execute(f"update wordle set guess2 = '{word_dex}' where username='{uname}'")
                        connecter.commit()
                        cur.execute(f"update wordle set guesses = 2 where username = '{uname}'")
                        connecter.commit()
                        return {"result":logic.letter_find(word), "attempts":"2/5"}
            if num ==  2:
                    word_dex = logic.letter_find(word)
                    try:
                        word_dex["error"]
                        return word_dex
                    except:
                        word_dex = str(word_dex).replace("'",'"')
                        if word == logic.get_word_day():
                            print(word_dex)
                            cur.execute(f"update wordle set guess5 = '{word_dex}' where username='{uname}'")
                            connecter.commit()
                            cur.execute(f"update wordle set guesses = 5 where username = '{uname}'")
                            connecter.commit()
                            return {"success":f"You guessed the correct word which is {logic.get_word_day()}"}

                        print(word_dex)
                        cur.execute(f"update wordle set guess3 = '{word_dex}' where username='{uname}'")
                        connecter.commit()
                        cur.execute(f"update wordle set guesses = 3 where username = '{uname}'")
                        connecter.commit()
                        return {"result":logic.letter_find(word), "attempts":"3/5"}

            if num == 3:
                    word_dex = logic.letter_find(word)
                    try:
                        word_dex["error"]
                        return word_dex
                    except:
                        word_dex = str(word_dex).replace("'",'"')
                        if word == logic.get_word_day():
                            print(word_dex)
                            cur.execute(f"update wordle set guess5 = '{word_dex}' where username='{uname}'")
                            connecter.commit()
                            cur.execute(f"update wordle set guesses = 5 where username = '{uname}'")
                            connecter.commit()
                            return {"success":f"You guessed the correct word which is {logic.get_word_day()}"}

                        print(word_dex)
                        cur.execute(f"update wordle set guess4 = '{word_dex}' where username='{uname}'")
                        connecter.commit()
                        cur.execute(f"update wordle set guesses = 4 where username = '{uname}'")
                        connecter.commit()
                        return {"result":logic.letter_find(word), "attempts":"4/5"}
            if num == 4:
                    word_dex = logic.letter_find(word)
                    try:
                        word_dex["error"]
                        return word_dex
                    except:
                        word_dex = str(word_dex).replace("'",'"')
                        if word == logic.get_word_day():
                            print(word_dex)
                            cur.execute(f"update wordle set guess5 = '{word_dex}' where username='{uname}'")
                            connecter.commit()
                            cur.execute(f"update wordle set guesses = 5 where username = '{uname}'")
                            connecter.commit()
                            return {"success":f"You guessed the correct word which is {logic.get_word_day()}"}
                        print(word_dex)
                        cur.execute(f"update wordle set guess5 = '{word_dex}' where username='{uname}'")
                        connecter.commit()
                        cur.execute(f"update wordle set guesses = 5 where username = '{uname}'")
                        connecter.commit()
                        return {"result":logic.letter_find(word), "attempts":"5/5", "word of the day":logic.get_word_day()}
            if num == 5:
                    return {"error":"you used all 5 attempts or you already gueesed one correct withen 5 attempts", "word of the day":logic.get_word_day()}
api.add_resource(TestLogin,"/test_login")
api.add_resource(SignUp,"/signup")
api.add_resource(Guess,"/word/<string:word>")

@app.route("/")
def index():
    return """
    /test_login - test if account is in database
    /signup - adds account into database
    /word/<randomword> - actuall wordle logic! replace '<ransomword>' with whatever word that you want!
    
    YOU ALWAYS HAVE TO MAKE SURE TO GO TO AUTHRIZATION IN POSTMAN AND CLICK BASIC AUTH TO TYPE IN CREDENTIALS!!!!!
    """
app.run(host="0.0.0.0",port=80)
