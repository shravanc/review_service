from app.helpers.composite.components.component import Component
class Composite(Component):
  
  def __init__(self):
    self._children = []

  def add(self, component):
    self._children.append(component)
    component.parent = None

  def operation(self, data):

    for child in self._children:
      print("----class---->", type(child))
      data = child.operation( data )


    #print("-->data-->", data)

    return data
    