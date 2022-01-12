from flask import Flask, render_template, jsonify, request
from datetime import datetime
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.hanghaegram


app = Flask(__name__)


@app.route('/categories')
def categorie():
    return render_template("categories_index.html")

@app.route('/categories/life')
def life():
    return render_template("life_index.html")

@app.route('/categories/sports')
def sports():
    return render_template("sports_index.html")

@app.route('/categories/travel')
def travel():
    return render_template("travel_index.html")

@app.route('/categories/food')
def food():
    return render_template("food_index.html")

@app.route('/categories/pet')
def pet():
    return render_template("pet_index.html")



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)