from flask import Flask, render_template

flaskapp = Flask(__name__)


@flaskapp.route('/')
def home():
    return render_template("home.html")


@flaskapp.route('/about/')
def about():
    return render_template("about.html")

@flaskapp.route('/map')
def map():
    return render_template("map.html")


if __name__ == "__main__":
    flaskapp.run(debug=True)
