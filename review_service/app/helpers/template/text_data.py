from app.helpers.template.template import Template

from app.helpers.composite.composite import Composite
from app.helpers.composite.components.languages.english import English
from app.helpers.composite.components.tokenizer.keras   import KerasTokenizer

class TextData(Template):

  def english_data(self): 
    english_branch = Composite()
    english_branch.add(English( ))
    english_branch.add(KerasTokenizer( ))

    return english_branch
