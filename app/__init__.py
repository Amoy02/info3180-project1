from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os.path import join,dirname,realpath


SECRET_KEY = 'Sup3r$3cretkey'

app = Flask(__name__)

app.config['SECRET_KEY'] = '\xee\xca\xb9.Q\xf7\xbd\xfe\xda|X\xfb\x93\x98\xdc\x15\x15(\x13z#D\xef\x1a\xb3'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://yourusername:yourpassword@localhost/databasename'

#Heroku Daatabase
app.config['SQLALCHEMY_DATABASE_URI']='postgres://posgkpzjfnremm:6b1a61f9e55afc2019b5452cbba6eb98c7b7a258a920ef0766a8989fd5b8a16c@ec2-52-87-135-240.compute-1.amazonaws.com:5432/d5ric48c6j7mlf'
#app.config['UPLOAD_FOLDER']= join(dirname(realpath(__file__)), 'static/uploads')


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

db = SQLAlchemy(app)

app.config.from_object(__name__)


from app import views
