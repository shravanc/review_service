from app.helpers.composite.components.component import Component

class AdamTraining(Component):
  EPOCHS = 10
  def __init__(self, x, y, model, epochs=EPOCHS):
    self.model = model
    self.x = x
    self.y = y
    self.epochs = epochs

  def opertion(self):
    self.model.compile(loss='binary_crossentropy',
                       optimizer="adam",
                       metrics=["accuracy"])

    self.model.fit(self.x, self.y, epochs=self.epochs)


