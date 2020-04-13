from abc import ABC, abstractmethod

class Component():

  @property
  def parent(self):
    return self._parent

  @parent.setter
  def parent(self, parent_comp):
    self._parent = parent_comp


  def add(self, component):
    pass
  
  def remove(self, component):
    pass

  @abstractmethod
  def operation(self):
    pass
