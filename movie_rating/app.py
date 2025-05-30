from flask import Flask
from controllers.movie import movie_bp

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Velkommen til Movie Rating App! Gå til <a href='/browse'>/browse</a></p>"

app.register_blueprint(movie_bp)
