class CareTaker:
  def __init__(self, originator):
    self._mementos    = []
    self._originator  = originator

  def backup(self):
    self._mementos.append(self._originator.save())

  def undo(self):
    if not len(self._mementos):
      return

    memento = self._mementos.pop()
    try:
      self._originator.restore(memento)
    except Exception:
      self.undo()

  def show_history(self):
    for memento in self._mementos:
      print(memento.get_name())

