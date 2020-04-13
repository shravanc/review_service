from app.helpers.composite.components.component import Component

import tensorflow as tf
from app import ml_model_path as model_path

class LSTM(Component):
  DEFAULT = model_path

  def __init__(self, path=DEFAULT):
    self.path = path

  def operation(self):
    return tf.keras.models.load_modules(self.path)

