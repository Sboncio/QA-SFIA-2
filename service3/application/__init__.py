# import Flask class from the flask module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
# create a new instance of Flask and store it in app 
app = Flask(__name__)


app.config['SECRET_KEY'] = str(os.getenv('SECRET_KEY_DB'))

app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://root:hannahandsam1@mysql:3306/sfia2"

db = SQLAlchemy(app)
from application import routes