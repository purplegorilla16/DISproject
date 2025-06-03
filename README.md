# DISproject

To run the web application do the following:

First run import_data.py and setup_ratings.py

Next start the virtual environment:
python -m venv .venv

Then activate it:
. .venv/bin/activate

Then install flask:
pip install flask

Lastly run the app:
flask run --debug

Open a browser and visit the sit http://127.0.0.1:5000


Once you enter the webb app, you can either register as a new user og choose among existing users. 
Afterwards you can choose among the top rated movies from and imdb datalist and give them your own rating and review. The rating will be saved in your username.
