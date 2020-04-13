from app import ml_model_path as model_path

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

vocab_size  = 10000
oov_tok     = "<OOV>"
max_len     = 120
trunc_type  = "post"
embedding_dim= 16
tokenizer   = Tokenizer(num_words=vocab_size, oov_token=oov_tok)

def tokenize(reviews):

  tokenizer.fit_on_texts(reviews)
  word_index  = tokenizer.word_index

  sequences   = tokenizer.texts_to_sequences(reviews)
  padded      = pad_sequences(sequences, maxlen=max_len)

  print(padded)
  return padded


def get_model():
  return tf.keras.models.load_model(model_path)


def preprocess_data(data):
  p_data = []
  for d in data:  
    print("-------------->", d)
    p_data.append( tokenize(d) )

  return p_data

def train_data(text, labels):
  data = tokenize(text)
  labels = np.array(labels)


  print(data)
  print(labels)

  model = get_model()
  model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

  num_epochs = 10
  model.fit(data, labels, epochs=num_epochs)

  model.save(model_path)


def prediction_to_labels(predictions):
  labels = []
  threshold= 0.2

  for pr in predictions:
    print('----->', pr)
    prob = round(round(pr[0], 2), 1)
    if prob > threshold:
      labels.append('Positive')
    else:
      labels.append('Negative')

  return labels

def predict_data(reviews):
  data = tokenize(reviews)
  model = get_model()

  predictions = model.predict(data)
  print(predictions)
  labels = prediction_to_labels(predictions)

  return labels

