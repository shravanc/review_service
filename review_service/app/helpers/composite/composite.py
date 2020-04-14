from app.helpers.composite.components.component import Component

from app.helpers.memento.originator import Originator
from app.helpers.memento.care_taker import CareTaker

class Composite(Component):
  
  def __init__(self, message=""):
    self._children  = []
    self.originator = Originator(message)
    self.caretaker  = CareTaker(self.originator)

  def add(self, component):
    self._children.append(component)
    component.parent = None

  def operation(self, obj):

    for child in self._children:
      print(child)
      obj = child.operation( obj )

    return obj


  def save_and_operate(self, obj):
    
    for child in self._children:
      self.originator.record(child)
      obj = child.operation( obj )
      self.caretaker.backup()

    return obj
