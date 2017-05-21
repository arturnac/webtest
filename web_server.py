from flask import Flask, render_template
from random import sample
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'rpi'
app.config['MONGO_URI'] = 'mongodb://35.166.238.215:27017'

mongo = PyMongo(app)

@app.route('/')
def index():
  return render_template('chart.html')

@aap.route('/')
def data():
	charts = mongo.db.charts
	result = charts.find()	
  return jsonify({'results' : results['CPU%']}) 

if __name__ == '__main__':
  app.run(debug=True)

