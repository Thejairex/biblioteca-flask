from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

from db import db
from models.book import Book
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def populate_database():
    df = pd.read_csv('Data/novels_clean.csv')
    for i, row in df.iterrows():
        book = Book(
            title=row['title'],
            description=row['description'],
            type=row['type'],
            region=row['region'],
            genres=row['genres'],
            tags=row['tags'],
            rating=row['rating'],
            release_year=row['release_year'],
            captions=row['captions'],
            completed=row['completed'],
            author=row['author']
        )
        db.session.add(book)
    db.session.commit()

with app.app_context():
    print('Creating tables...')
    db.create_all()
    print('Populating database...')
    populate_database()
    
    

@app.route('/')
def index():
    return "Hello World!"


@app.route('/books')
def books():
    books = Book.query.all()
    return str(books)

if __name__ == '__main__':
    app.run(debug=True)