
from app.helpers.composite.components.component import Component
from app import ml_model_path as model_path


class Local(Component):
  DEFAULT = model_path
  def __init__(self, path=DEFAULT):
    self.model  = None
    self.path   = path

  def operation(self, obj):
    self.model = obj.model
    self.model.save(self.path)

    return obj.labels
