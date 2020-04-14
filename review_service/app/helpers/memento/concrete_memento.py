from app.helpers.memento.memento import Memento

from datetime import datetime

class ConcreteMemento(Memento):
  def __init__(self, state=""):
    self._state = state
    self._date  = str(datetime.now())[:19]

  def get_state(self):
    return self._state

  def get_name(self):
    return f"{self._date} / ({self._state[0:9]}...)"

  def get_date(self):
    return self._date



