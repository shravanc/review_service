from flask import request, jsonify, render_template

from app.helpers.train import train_data, predict_data
from app.helpers.composite.client import Client

def index():
  engine = MovieReview()
  sentiments = engine.get_Sentiment('lstm')
  return jsonify({'data': sentiments})

def train():
  print("***inside***")
  data = request.get_json()
  print("data****************>", data)
  train_data( data['reviews'], data['labels'] ) 

  return jsonify( {'message': 'Training successful'} )

def predict():
  data = request.get_json()

  ct = Client()
  predictions = ct.operate( data['reviews'] )

  #predictions = predict_data(data['reviews']) 
  return jsonify( {'predictions': {'reviews': data['reviews'], 'predictions': [predictions]}} )


def home():
  return render_template('index.html')

