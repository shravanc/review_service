from app import db

class Genre(db.Model):
  __tablename__ = 'genres'
  __bind_key__  = 'db2'


  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String)

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def count(self):
    return Genre.query.count()

  def get_genres(self):
    genres = Genre.query.all()
    genre_list = []
    for genre in genres:
      genre_list.append(genre.title)
  
    return genre_list
