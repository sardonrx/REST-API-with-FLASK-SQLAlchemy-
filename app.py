from enum import unique
from flask import Flask, config, request, jsonify 
from  flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
import os

app = Flask(__name__)
basedir= os.path.abspath(os.path.dirname(__file__))
#database
app.config['SQLALCHEMY_DATABASE_URL']='sqlite:///'+ os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
#init db
db = SQLAlchemy(app)
#init ma 
ma = Marshmallow(app)
#product class
class Product(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String, unique = True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.column(db.Integer)


def __init__(self, name, description, price, qty):
    self.name = name
    self.description = description
    self.price = price
    self.qty = qty


#productschema 
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description','price' 'qty')

#initschema

product_schema = ProductSchema()
products_schema = ProductSchema(many= True, )







if __name__ == '__main__': 
    app.run(debug=True)
