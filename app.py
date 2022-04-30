import flask
from flask import Flask
import data
import random

app = Flask(__name__)


@app.get("/")
def tell_a_joke():
    joke = random.choice(data.jokes)
    return flask.render_template('joke.html', joke_text=joke)
