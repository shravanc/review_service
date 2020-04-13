from app.helpers.composite.components.component import Component

class SentimentPrediction(Component):
  THRESHOLD = 0.1

  def __init__(self, threshold=THRESHOLD):
    self.texts = None
    self.model = None
    self.predictions = None
    self.labels      = []
    self.threshold   = threshold

  def operation(self, obj):
    self.model = obj.model
    self.texts = obj.texts
    self.predictions = self.model.predict( self.texts )
    self.__prediction_to_labels()
    return self

  #private
  def __prediction_to_labels(self):
    for pr in self.predictions:
      prob = round(round(pr[0], 2), 1)
      if prob > self.threshold:
        self.labels.append('Positive')
      else:
        self.labels.append('Negative')


