from abc import ABC, abstractmethod
from string import ascii_letters, digits
from random import sample

from app.helpers.memento.concrete_memento import ConcreteMemento

class Originator():
  _state = None

  def __init__(self, state=""):
    self._state = state

  def record(self, obj):
    self._state = self._generate_random_string(30)

  def _generate_random_string(self, length):
    return "".join(sample(ascii_letters, length))

  def save(self):
    return ConcreteMemento(self._state)

  def restore(self, memento):
    self._state = memento.get_state()


