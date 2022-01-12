from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dblife


app = Flask(__name__)


@app.route('/')
def main():
    return render_template("categories_index.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)