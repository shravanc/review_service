from app.helpers.composite.components.component import Component

class Hindi(Component):
  def __init__(self, data):
    self.data = data

  def operation(self):
    return self.__preprocess()

  #private
  def __preprocess(self):
    return self.data


