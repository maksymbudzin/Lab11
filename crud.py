from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from models.AbstractTour import AbstractTour
import os
import json
import copy

with open('secret.json') as f:
    SECRET = json.load(f)

SQLALCHEMY_TRACK_MODIFICATIONS = False
DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Tour(AbstractTour, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=False)
    operator = db.Column(db.String(32), unique=False)
    top_price = db.Column(db.Integer, unique=False)
    base_price = db.Column(db.Integer, unique=False)
    type_of_accomodation = db.Column(db.String(32), unique=False)
    numbers_of_family = db.Column(db.String(32), unique=False)

    def __init__(self, name='N/A', operator='N/A', top_price=0, base_price=0,
                 type_of_accomodation='N/A', numbers_of_family=0):
        super().__init__(name, operator, top_price, base_price)
        self.type_of_accomodation = type_of_accomodation
        self.numbers_of_family = numbers_of_family


class TourSchema(ma.Schema):
    class Meta:
        fields = ('name', 'operator',
                  'top_price', 'base_price', 'type_of_accomodation',
                  'numbers_of_family')


tour_schema = TourSchema()
tours_schema = TourSchema(many=True)


@app.route("/tour", methods=["POST"])
def add_tour():
    name = request.json['name']
    operator = request.json['operator']
    top_price = request.json['top_price']
    base_price = request.json['base_price']
    type_of_accomodation = request.json['type_of_accomodation']
    numbers_of_family = request.json['numbers_of_family']
    tour = Tour(name,
                          operator,
                          top_price,
                          base_price,
                          type_of_accomodation,
                          numbers_of_family)
    db.session.add(tour)
    db.session.commit()
    return tour_schema.jsonify(tour)


@app.route("/tour", methods=["GET"])
def get_all_tours():
    all_tours = Tour.query.all()
    result = tours_schema.dump(all_tours)
    return jsonify({'tour_appliances': result})


@app.route("/tour/<id>", methods=["GET"])
def get_tour(id):
    tour = Tour.query.get(id)
    if not tour:
        abort(404)
    return tour_schema.jsonify(tour)


@app.route("/tour/<id>", methods=["PUT"])
def update_tour(id):
    tour = Tour.query.get(id)
    if not tour:
        abort(404)
    old_tour = copy.deepcopy(tour)
    tour.name = request.json['name']
    tour.operator = request.json['operator']
    tour.top_price = request.json['top_price']
    tour.base_price = request.json['base_price']
    tour.type_of_accomodation = request.json['type_of_accomodation']
    tour.numbers_of_family = request.json['numbers_of_family']
    db.session.commit()
    return tour_schema.jsonify(old_tour)


@app.route("/tour/<id>", methods=["DELETE"])
def tour_delete(id):
    tour = Tour.query.get(id)
    if not tour:
        abort(404)
    db.session.delete(tour)
    db.session.commit()
    return tour_schema.jsonify(tour)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='127.0.0.1')
