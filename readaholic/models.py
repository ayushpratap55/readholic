from readaholic import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)
class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(60), nullable=False)
    password=db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return f"User(email: {self.email})"


class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(120), unique=True, nullable=False)
    author_name = db.Column(db.String(80), nullable=False)
    shop_link = db.Column(db.String(100), nullable=True)
    genre = db.Column(db.String(30), nullable=True)
    cover_image_file = db.Column(db.String(50), nullable=False, default="default.jpeg")
    tiny_summary = db.Column(db.Text, nullable=True)
    isbn = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Book(Title: '{self.book_title}', Author: '{self.author_name}', Cover Image: '{self.cover_image_file}', ISBN Number: '{self.isbn}')"

