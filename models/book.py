from db import db

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=True)
    type = db.Column(db.String(80), nullable=False)
    region = db.Column(db.String(80), nullable=False)
    genres = db.Column(db.String(80), nullable=False)
    tags = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    captions = db.Column(db.Integer, nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    author = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title