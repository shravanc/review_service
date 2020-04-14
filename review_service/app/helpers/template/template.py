from app.helpers.composite.composite import Composite

from abc import ABC, abstractmethod


class Template:
  def __init__(self):
    self.tree = Composite()
    self.branches = []
    self.texts    = None
    self.labels   = None

  def prediction_template(self, texts):
    self.texts = texts

    self.branches.append(self.text_data())
    self.branches.append(self.prediction())

    self.add_branches()
    self.operate()

    return self.response_format()


  def training_template(self, texts, labels):
    self.texts  = texts
    self.labels = labels
  
    self.branches.append(self.text_data())
    self.branches.append(self.train())

    self.add_branches()
    self.operate()

    return self.response_format()

    
  def add_branches(self):
    for branch in self.branches:
      self.tree.add(branch)

  def operate(self):
    #self.resp = self.tree.operation( self )
    self.resp = self.tree.save_and_operate( self )


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

