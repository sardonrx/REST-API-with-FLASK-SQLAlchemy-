from flask import Flask, request, jsonify 
from  flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
import os


app = Flask(__name__)

basedir= os.path.abspath(os.path.dirname(__file__))
#database
app.config['SQLALCHEMY_DATABASE_URL']='sqlite:///'+ os.path.join(basedir, 'db.aqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
#init db
db = SQLAlchemy(app)
#init ma 
ma = Marshmallow(app)


if __name__ == '__main__':
    app.run(debug=True)
