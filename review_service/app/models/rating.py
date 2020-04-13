from app import db
from app.models.items import Item
from sqlalchemy.dialects.postgresql import JSON
import pandas as pd
import tensorflow as tf

from app.helpers.decorator.default              import Default
from app.helpers.decorator.db_to_dict           import DbToDict
from app.helpers.decorator.dict_to_data_frame   import DictToDataFrame
from app.helpers.decorator.df_to_features       import DFToFeatures
from app.helpers.decorator.features_to_tensors  import FeaturesToTensor

from app.helpers.schema import get_schema


class Rating(db.Model):
  __tablename__ = 'ratings'
  __bind_key__  = 'db1'
  

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer)
  item_id = db.Column(db.Integer)
  rating  = db.Column(db.Integer)

  def __init__(self):
    self.columns = ['id', 'user_id', 'item_id', 'rating']

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def all_user_ratings(self):
    Rating.__table__.schema = get_schema()
    all_ratings = Rating.query.all()
    ratings = []
    for rating in all_ratings:
      data = {}
      data["user_id"] = rating.user_id
      data["item_id"] = rating.item_id
      data["rating"]  = rating.rating
      ratings.append(data)
  
    return ratings

  def get_user_items(self):
    ratings = self.all_user_ratings()
    total_movies = len(Item().get_item_names())    
   
    print("*********>", ratings) 
    features = pd.DataFrame(ratings).groupby('user_id')
    user_ratings = []
    for user_id, df in features:
      data = [0] * total_movies
      for index, item in df.iterrows():
        data[item.item_id-1] = item.rating

      user_ratings.append(data)

    return tf.constant(user_ratings, dtype=tf.float32)


  """
  def get_user_items(self):
    ratings = self.all_user_ratings()
    ratings = Rating.query.all()

    total_movies = Item().count() #get_item_names())    
 
    print("-----------------------------get_user_items------------------------------------") 
    #return  FeaturesToTensor(
    #                          DFToFeatures(
    df = DictToDataFrame(
                                  DbToDict(
                                    Default(ratings), self.columns
                                  )
                                ). operation #, total_movies, 'rating'
                              #)
                            #).operation()
    data = [0] * total_movies
    user_ratings = []
    for index, item in df,iterrows():
      datap[item.item_id-1] = item.rating
      
  """

