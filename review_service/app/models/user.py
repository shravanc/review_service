from app import db
from sqlalchemy.dialects.postgresql import JSON

from app.helpers.schema import get_schema


class User(db.Model):
  __tablename__ = 'users'
  __bind_key__  = 'db1'
  __table_args__ = {'extend_existing': True} 


  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String)

  def __repr__(self):
    return '<id {}>'.format(self.id)


  def get_usernames(self):
    User.__table__.schema = get_schema()

    users = User.query.all()
    user_list = []
    for user in users:
      user_list.append(user.username)

    return user_list


  def all_users(self):
    User.__table__.schema = get_schema()
    users = User.query.all()
    user_list = []
    for user in users:
      d1["id"] = user.id
      d1["usernam"] = user.username
      user_list.append(d1)

    return user_list

  def count(self):
    User.__table__.schema = get_schema()
    return User.query.count()


