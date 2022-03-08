Hi there, I created a rest api on wordle using a language called Python and a SQL database called PostgreSQL. It's just Wordle but you manipulate via url.

Github repo: https://github.com/anishgorakavi787809/rest-wordle



Requirements:

Python 3.10 - as I used match, case statements

PostgreSQL

Postman



How to run:

clone the github repository

open psql or pgadmin4 and create a database called wordle-rest

then create a table called login which has 2 columns which is: username, type: text, password, type: text.

Create a table called wordle which has 7 columns: username; type: text guesses; type: integer; guess1, type: json; guess2, type: json; guess3, type: json; guess4, type:json; guess5,type: json

Now go to server.py, change the following line from line 7:

connecter = psycopg2.connect(user="postgres",password="Checkred",host="127.0.0.1",database="wordle-rest")

TO

connecter = psycopg2.connect(user="postgres",password="<your password> - change this",host="127.0.0.1",database="wordle-rest")

then, go and type (python3.10 if linux or /usr/local/bin/python3 if mac, or python3 if windows) -m pip install random-word flask psycopg2 flask-restful pyyaml

Finally, go and type (python3.10 if linux or /usr/local/bin/python3 if mac, or python3 if windows) server.py

Go to postman and type localhost. It should give a list of urls. Go to authorization tab and click on No auth and options should show.

CLICK ON BASIC AUTH!!!!!!

and put in the username and password

then in the url, type in: localhost/signup and it will put the account you typed into the database

In url type in localhost/wordle/<the word you choose> to play the REST api version of wordle.

Now, if you want, put my code in a aws server so, everyone can have the api to build apps with.



If you have any code suggestions or wanna change code, reply below!
