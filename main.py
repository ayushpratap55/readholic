from flask import Flask, render_template
from forms import AdminRegistrationForm
from forms import AdminLoginForm

app = Flask(__name__)

msg='Ayush Pratap'

website_name="Readaholic"
data={
    "website_name":"Readaholic",
    "author":"Ayush"
}

app.config['SECRET_KEY']= 'secret_key33'

@app.route("/")
def home():
    #rendering(returning) HTML file
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    #rendering(returning) HTML file
    form = AdminRegistrationForm()
    if form.validate_on_submit():
        print(form.data)
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    #rendering(returning) HTML file
    form = AdminLoginForm()
    if form.validate_on_submit():
        print(form.data)
    return render_template("login.html", form=form)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/me")     
@app.route("/add")
@app.route("/place")        #grouping all routes together
def place():
    return f"<h1>Hello, Ayush Pratap</h1>"

if __name__ == "__main__":
    app.run(debug=True)