from app.helpers.composite.components.component import Component

class English(Component):
  def __init__(self):
    self.texts  = None
    self.labels = None

  def operation(self, obj):
    self.labels = obj.labels
    return self.__preprocess(obj.texts)


  #Private
  def __preprocess(self, texts):
    print("--------English-----------")
    self.texts = texts
    return self
