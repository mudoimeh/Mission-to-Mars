#import sys
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import Scrape_Mars

app = Flask(__name__)

client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_facts

@app.route('/')
def index():
    mars = mongo.db.mars.find_one()
    return render_template('index.html', mars=mars)

@app.route('/scrape')
def scrape():
    mars = mongo.db.mars
    data = Scrape_Mars.scrape()
    mars.update({}, data, upsert=True)
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)