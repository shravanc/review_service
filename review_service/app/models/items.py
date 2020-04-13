from app import db
from sqlalchemy.dialects.postgresql import JSON
import pandas as pd
import tensorflow as tf
from app.models.genre import Genre


from app.helpers.decorator.default              import Default
from app.helpers.decorator.db_to_dict           import DbToDict
from app.helpers.decorator.dict_to_data_frame   import DictToDataFrame
from app.helpers.decorator.df_to_features       import DFToFeatures
from app.helpers.decorator.features_to_tensors  import FeaturesToTensor

from app.helpers.schema import get_schema

class Item(db.Model):
  __tablename__ = 'items'
  __bind_key__  = 'db2'
  __mapper_args__ = {
      'include_properties' :['id', 'title', 'genres']
  }

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String)
  description = db.Column(db.String)
  state = db.Column(db.String)
  genres = db.Column(db.ARRAY(db.Integer))

  def __init__(self):
    self.columns = ['id', 'title', 'description', 'state', 'genres']

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def count(self):
    Item.__table__.schema = get_schema()
    return Item.query.count()

  def get_item_names(self):
    Item.__table__.schema = get_schema()
    items = Item.query.all()
    titles = []
    for item in items:
      titles.append(item.title)
  
    return titles

  def all_items(self):
    Item.__table__.schema = get_schema()
    items = Item.query.all()
    data = []
    titles = []

    for item in items:
      for k in ['id', 'title', 'genres']:
        d1 = {}
        d1[k]    = getattr(item, k)
      
      data.append(d1)
      titles.append(item.title)
  
    return data, titles


  def get_items_features1(self):
    items, title = self.all_items()
    total_item_feats = Genre().count()

    df = pd.DataFrame(items)
    features = []
    for index, item in df.iterrows():
      one_hot = [0] * total_item_feats
      for i in item.genres:
        one_hot[i-1] = 1
      features.append(one_hot)

    return tf.constant(features, dtype=tf.float32)




  def get_items_features(self): #_using_decorator(self):

    print("------>doamin***********", get_schema())
    Item.__table__.schema = get_schema()

    items = Item.query.all()
    number_of_features = Genre().count()
    return FeaturesToTensor( 
                      DFToFeatures( 
                        DictToDataFrame( 
                          DbToDict( 
                            Default(items), self.columns
                          )
                        ), number_of_features, 'genres'
                      )   
                    ).operation()






