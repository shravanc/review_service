from app.helpers.composite.components.component import Component

import tensorflow as tf
from app import ml_model_path as model_path


class Simple(Component):
  DEFAULT = model_path

  def __init__(self, path=DEFAULT):
    self.path   = path
    self.model  = None 

  def operation(self, obj=None):
    self.model  = tf.keras.models.load_model(self.path)
    self.texts  = obj.padded
    self.labels = obj.labels
    return self

