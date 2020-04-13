from app.helpers.template.template import Template

from app.helpers.composite.composite import Composite
from app.helpers.composite.components.models.simple           import Simple
from app.helpers.composite.components.predictions.sentiment   import SentimentPrediction
from app.helpers.composite.components.saving.local            import Local

class Prediction(Template):
  
  def prediction(self):
    model_branch = Composite()
    model_branch.add(Simple())
    model_branch.add(SentimentPrediction())
    model_branch.add(Local())

    return model_branch 

  def response_formate(self):
    return []
