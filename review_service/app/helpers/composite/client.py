#Components
from app.helpers.composite.components.languages.english       import English
from app.helpers.composite.components.models.simple           import Simple
from app.helpers.composite.components.predictions.sentiment   import SentimentPrediction
from app.helpers.composite.components.saving.local            import Local
from app.helpers.composite.components.tokenizer.keras         import KerasTokenizer
from app.helpers.composite.components.training.adam_training  import AdamTraining

#from app.helpers.composite.components. import
#from app.helpers.composite.components. import
from app.helpers.composite.composite import Composite

class Client:
  def __init__(self,):
    self.tree = Composite()

    self.english_branch = Composite()
    self.english_branch.add(English( ))
    self.english_branch.add(KerasTokenizer( ))

    self.model_branch = Composite()
    self.model_branch.add(Simple())
    self.model_branch.add(SentimentPrediction())
    self.model_branch.add(Local())
        

    self.tree.add(self.english_branch)
    self.tree.add(self.model_branch)


  def operate(self, texts):
    result = self.tree.operation(texts)
    print(result)
    return result


