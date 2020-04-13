from app import db
from sqlalchemy.dialects.postgresql import JSON

from app.helpers.schema import get_schema

class Review(db.Model):
  __tablename__ = 'reviews'
  __bind_key__  = 'db1' 
  __table_args__ = {'extend_existing': True}


  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String)

  def __repr__(self):
    return '<id {}>'.format(self.id)

