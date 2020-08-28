# import Flask class from the flask module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
# create a new instance of Flask and store it in app 
app = Flask(__name__)

app.config['SECRET_KEY'] = "secret_key"
#str(os.getenv('SECRET_KEY_DB'))
app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://root:hannahandsam1@mysql:3306/sfia2"
#str(os.getenv('DATABASE_URI'))
db = SQLAlchemy(app)
# import the ./application/routes.py file
from application import routes