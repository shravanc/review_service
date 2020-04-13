from app.helpers.composite.components.component import Component

class English(Component):
  def __init__(self):
    self.texts = None

  def operation(self, texts):
    return self.__preprocess(texts)


  #Private
  def __preprocess(self, texts):
    print("--------English-----------")
    self.texts = texts
    return self
