from flask import render_template, flash, redirect, url_for
from readaholic.forms import AdminLoginForm, AdminRegistrationForm
from readaholic import app, db, bcrypt
from readaholic.models import User


@app.route("/")
def home():
    #rendering(returning) HTML file
    return render_template("home.html")

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
                flash("Successfully logged in", "success")
                return redirect(url_for("home"))
            else:
                flash("You've entered wrong password, please try again!")
    
    return render_template("login.html", form=form)

# @app.route("/addbook", methods=["GET", "POST"])
# def addbook():
#     #rendering(returning) HTML file
#     form = AdminRegistrationForm()
#     if form.validate_on_submit():
#         print(form.data)
#     return render_template("addbook.html", form=form)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/me")     
@app.route("/add")
@app.route("/place")        #grouping all routes together
def place():
    return f"<h1>Hello, Ayush Pratap</h1>"