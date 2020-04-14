from abc import ABC, abstractmethod

class Memento():

  @abstractmethod
  def get_name(self):
    pass

  @abstractmethod
  def get_date(self):
    pass


