from app.helpers.composite.components.component import Component

import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

class KerasTokenizer(Component):

  VOCAB_SIZE = 1000
  OOV_TOKEN  = "<OOV>"
  MAX_LEN    = 120
  TRUNC_TYPE = "post"
  EMBED_DIM  = 16


  def __init__( self, 
                vocab_size=VOCAB_SIZE,
                oov_token=OOV_TOKEN,
                max_len=MAX_LEN,
                trunc_type=TRUNC_TYPE,
                embed_dim=EMBED_DIM, 
               ):

    self.texts      = None
    self.labels     = None
    self.vocab_size = vocab_size
    self.oov_token  = oov_token
    self.max_len    = max_len
    self.trunc_type = trunc_type
    self.embd_dim   = embed_dim

    self.tokenizer  = Tokenizer(num_words=self.vocab_size,
                                oov_token=self.oov_token)

  

  def operation(self, obj=None):
    print("--------KERAS-----------")
    self.texts  = obj.texts
    self.labels = obj.labels
    if obj.labels is not None:
      self.labels = np.array(obj.labels)

    self.tokenizer.fit_on_texts(self.texts)
    
    sequences = self.tokenizer.texts_to_sequences(self.texts)
    padded    = pad_sequences(sequences, maxlen= self.max_len)

    self.padded = padded
    return self




