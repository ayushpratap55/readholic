from flask import render_template, flash, redirect, url_for, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from readaholic.forms import AdminLoginForm, AdminRegistrationForm, AddBookForm
from readaholic import app, db, bcrypt
from readaholic.models import User, Book
import os
from uuid import uuid4


@app.route("/")
@login_required
def home():
    book_data=Book.query.all()
    #rendering(returning) HTML file
    return render_template("home.html", data=book_data)

@app.route("/register", methods=["GET", "POST"])
def register():
    
    form = AdminRegistrationForm()
    if form.validate_on_submit():
        _email=form.data['email']
        _password=form.data['password']
        _password = bcrypt.generate_password_hash(_password).decode("utf-8")
        user=User(email=_email, password=_password)
        try:
            db.session.add(user)
            db.session.commit()
            flash("Account successfully created, you may now login","success")
            return redirect(url_for("login"))
        except:
            flash("Something went wrong with database", "warning")

    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    #rendering(returning) HTML file
    form = AdminLoginForm()
    if form.validate_on_submit():
        _email = form.data['email']
        _password = form.data['password']
        user = User.query.filter_by(email=_email).first()
        if not user:
            flash(f"No user with email{_email} found! Register now.", "danger")
            return redirect(url_for("register"))
        else:
            if bcrypt.check_password_hash(user.password, _password):
                login_user(user)
                flash("Successfully logged in", "success")
                return redirect(url_for("home"))
            else:
                flash("You've entered wrong password, please try again!")
    
    return render_template("login.html", form=form)

@app.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    flash("You've successfully logged out", "success")
    return redirect(url_for("login"))

def save_cover_image(cover_image):
    f = cover_image.data
    filename = f"picture-{str(uuid4())}.{f.filename.split('.')[1].lower()}"
    f.save(os.path.join(app.instance_path, "uploads", filename))
    return filename


@app.route("/addbooks", methods=["GET", "POST"])
def addbooks():
    #rendering(returning) HTML file
    form = AddBookForm()
    if form.validate_on_submit():
        _book_title=form.data['book_title']
        _author_name=form.data['author_name']
        _cover_image_file=save_cover_image(form.cover_image_file)
        _isbn=form.data['isbn']
        _genre=form.data['genre']
        _rating=form.data['rating']
        _shop_link=form.data['shop_link']
        _tiny_summary=form.data['tiny_summary']
        book=Book(
            book_title=_book_title,
            author_name=_author_name, 
            cover_image_file=_cover_image_file, 
            isbn=_isbn, 
            genre=_genre, 
            rating=_rating, 
            shop_link=_shop_link, 
            tiny_summary=_tiny_summary
        )
        try:
            db.session.add(book)
            db.session.commit()
            flash("Book successfully added","success")
        except:
            flash("Something went wrong while adding", "warning")
        print(form.data)
    return render_template("addbooks.html", form=form)

@app.route("/uploads/<filename>")
def send_image_file(filename):
    return send_from_directory(os.path.join(app.instance_path, "uploads"), filename)

@app.route("/book/<isbn>", methods=["GET"])
def get_book(isbn):
    book = Book.query.filter_by(isbn=isbn).first()
    if not book:
        flash("Book not found")
        return redirect(url_for('home'))
    else:
        return render_template("book.html", data=book)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/me")     
@app.route("/add")
@app.route("/place")        #grouping all routes together
def place():
    return f"<h1>Hello, Ayush Pratap</h1>"