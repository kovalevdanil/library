from lib import db
import os

book_genre = db.Table('book_genre',
                      db.Column('book_id', db.Integer,
                                db.ForeignKey('book.id')),
                      db.Column('genre_id', db.Integer, db.ForeignKey('genre.id')))

book_shelf = db.Table('book_shelf', 
                      db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
                      db.Column('shelf_id', db.Integer, db.ForeignKey('shelf.id')))

user_shelf = db.Table('user_shelf',
                      db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                      db.Column('shelf_id', db.Integer, db.ForeignKey('shelf.id')))

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), default='Undefined')
    info = db.Column(db.Text, default='')
    rate = db.Column(db.Float, default=0)
    read = db.Column(db.Integer, default=0)
    cover_art_path = db.Column(db.String(128))
    file_path = db.Column(db.String(128))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    # author = db.relationship("Author", backref='book')
    genres = db.relationship(
        'Genre', secondary=book_genre)

    def __repr__(self):
        return '<Book; ID: {0}; Title: \'{1}\'>'.format(self.id, self.title)


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    birth = db.Column(db.Date)
    info = db.Column(db.Text, default='')
    language = db.Column(db.String(20))

    books = db.relationship('Book', backref = 'author')

    def __repr__(self):
        return "<Author; ID: {0}; Name: {1}>".format(self.id, self.name)


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))

    books = db.relationship(
        'Book', secondary=book_genre)

    def __repr__(self):
        return "<Gengre; ID: {0}; Name: {1}>".format(self.id, self.name)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), unique = True, nullable = False)
    password_hash = db.Column(db.String(128), nullable = False)
    avatar_path = db.Column(db.String(32), nullable = False, default = 'default.jpg')

    shelves = db.relationship('Shelf', secondary = user_shelf)

    def __repr__(self):
        return "<User; ID {0}; name {1}>".format(self.id, self.name)

class Shelf(db.Model):
    __tablename__ = 'shelf'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    books = db.relationship('Book', secondary = book_shelf)
    users = db.relationship('User', secondary = user_shelf)

    def __repr__(self):
        return '<Shelf; ID {0}; name {1}>'.format(self.id, self.name)
