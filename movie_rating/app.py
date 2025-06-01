from flask import Flask
from database import init_ratings
from controllers.movie import movie_bp

init_ratings()

app = Flask(__name__)
app.register_blueprint(movie_bp)
