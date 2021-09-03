# import "packages" from flask
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

# connects default URL to render about.html
@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/games/')
def games():
    return render_template("games.html")

@app.route('/aboutAidan/')
def aboutAidan():
    return render_template("aboutAidan.html")

@app.route('/aboutArch/')
def aboutArch():
    return render_template("aboutArch.html")

@app.route('/aboutDavid/')
def aboutDavid():
    return render_template("aboutDavid.html")

@app.route('/aboutTyler/')
def aboutTyler():
    return render_template("aboutTyler.html")

@app.route('/aboutWilliam/')
def aboutWilliam():
    return render_template("aboutWilliam.html")



# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
