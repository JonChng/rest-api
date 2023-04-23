from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

def create_dict(query):
    #Pass in query in return dictionary
    to_return = {
        "id":query.id,
        "name":query.name,
        "map_url": query.map_url,
        "img_url": query.img_url,
        "location": query.location,
        "seats": query.seats,
        "has_toilet": query.has_toilet,
        "has_wifi": query.has_wifi,
        "has_sockets": query.has_sockets,
        "can_take_calls": query.can_take_calls,
        "coffee_price": query.coffee_price
    }

    return to_return

db.create_all()
@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    cafe = random.choice(cafes)
    cafe_details = create_dict(cafe)
    return jsonify(cafe_details)

@app.route("/all", methods=["GET"])
def all():
    cafes = db.session.query(Cafe).all()
    cafes_1 = {"cafes":[]}

    for i in cafes:
        cafes_1["cafes"].append(create_dict(i))
    print(cafes_1)
    return jsonify(cafes_1)

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
