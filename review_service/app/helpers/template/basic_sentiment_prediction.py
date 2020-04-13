from app.helpers.template.template import Template

from app.helpers.composite.composite import Composite
from app.helpers.composite.components.languages.english import English
from app.helpers.composite.components.tokenizer.keras   import KerasTokenizer

from app.helpers.composite.components.models.simple           import Simple
from app.helpers.composite.components.predictions.sentiment   import SentimentPrediction
from app.helpers.composite.components.saving.local            import Local

class BasicSentimentPrediction(Template):

  def __init__(self):
    super(BasicSentimentPrediction, self).__init__()

  def text_data(self):
    english_branch = Composite()
    english_branch.add(English( ))
    english_branch.add(KerasTokenizer( ))

    return english_branch


  def prediction(self):
    model_branch = Composite()
    model_branch.add(Simple())
    model_branch.add(SentimentPrediction())
    model_branch.add(Local())

    return model_branch

