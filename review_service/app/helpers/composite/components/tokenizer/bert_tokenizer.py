from app.helpers.composite.components.component import Component

from bert.tokenization.bert_tokenization import FullTokenizer


class BertTokenizer(Component):
  def __init__( self,
                texts,
                vocab_size=VOCAB_SIZE,
                oov_token=OOV_TOKEN,
                max_len=MAX_LEN,
                trunc_type=TRUNC_TYPE,
                embed_dim=EMBED_DIM,
               ):

    self.texts = texts
    self.tokenizer = FullTokenizer


  def opertion(self):
    return self.tokenizer.tokenize(self.texts)
