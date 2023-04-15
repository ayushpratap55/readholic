from flask import Flask, render_template

app = Flask(__name__)

msg='Ayush Pratap'

website_name="Readaholic"
data={
    "website_name":"Readaholic",
    "author":"Ayush"
}

@app.route("/")
def home():
    #rendering(returning) HTML file
    return render_template("home.html")


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