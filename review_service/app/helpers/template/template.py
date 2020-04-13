from app.helpers.composite.composite import Composite

from abc import ABC, abstractmethod


class Template:
  def __init__(self):
    print("****called****")
    self.tree = Composite()
    self.branches = []

  def prediction_template(self, texts):
    self.texts = texts

    self.branches.append(self.text_data())
    self.branches.append(self.prediction())

    print("***before_add***")
    self.add_branches()
    print("***after_add***")
    self.operate()

    return self.response_format()


  def add_branches(self):
    for branch in self.branches:
      self.tree.add(branch)

  def operate(self):
    self.resp = self.tree.operation( self.texts )

  def response_format(self):
    return self.resp

  @abstractmethod
  def text_data(self):
    pass

  @abstractmethod
  def prediction(self):
    pass

  @abstractmethod
  def train(self):
    pass

