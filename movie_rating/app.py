from flask import Flask
from database import init_db
from controllers.movie import movie_bp

init_db()

app = Flask(__name__)
app.register_blueprint(movie_bp)
