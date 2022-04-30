import flask
from flask import Flask
from data import jokes
import random

app = Flask(__name__)


@app.get("/")
def tell_a_joke():
    print("Begging to tell a joke!")
    joke = random.choice(jokes)
    print(f"The joke we are telling is {joke}")
    return flask.render_template('joke.html', joke_text=joke)
