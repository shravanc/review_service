from app.helpers.composite.components.component import Component

class AdamTraining(Component):
  EPOCHS = 10
  def __init__(self, epochs=EPOCHS):
    self.model  = None
    self.texts  = None
    self.labels = None
    self.epochs = epochs

  def operation(self, obj):

    self.model  = obj.model
    self.texts  = obj.texts
    self.labels = obj.labels

    self.model.compile(loss='binary_crossentropy',
                       optimizer="adam",
                       metrics=["accuracy"])

    self.model.fit(self.texts, self.labels, epochs=self.epochs)
    return self

