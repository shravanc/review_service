from flask import request, jsonify, render_template

from app.helpers.train import train_data, predict_data
from app.helpers.template.basic_sentiment_prediction import BasicSentimentPrediction
from app.helpers.template.train import Train

def index():
  engine = MovieReview()
  sentiments = engine.get_Sentiment('lstm')
  return jsonify({'data': sentiments})

def train():
  data = request.get_json()

  temp = Train()
  temp.training_template(data['reviews'], data['labels'])


  #train_data( data['reviews'], data['labels'] ) 

  return jsonify( {'message': 'Training successful'} )

def predict():
  data = request.get_json()

  temp = BasicSentimentPrediction()
  predictions = temp.prediction_template(data['reviews'])

  return jsonify( {'predictions': {'reviews': data['reviews'], 'predictions': [predictions]}} )


def home():
  return render_template('index.html')

