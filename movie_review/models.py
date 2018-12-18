from datetime import datetime
from movie_review import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# sql: models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Review', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)

    def __repr__(self):
        return f"Review('{self.title}', '{self.rate}', '{self.date_posted}')"


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    date_released = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(100), nullable=False)
    cast = db.Column(db.String(100), nullable=False)
    info = db.Column(db.Text, nullable=False, default='Introduction of the movie is missing right now')
    reviews = db.relationship('Review', backref='movie', lazy=True)

    def __repr__(self):
        return f"Movie('{self.name}', '{self.date_released}', '{self.type}', '{self.cast}')"

