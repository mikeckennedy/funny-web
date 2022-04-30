import flask
from flask import Flask
import random

app = Flask(__name__)

jokes = [
    "Relationship status? I'll leave the relations to the database.",
    "How do you get the code for the bank vault? You checkout their branch.",
    "What diet did the ghost developer go on? Boolean",
]


@app.get("/")
def tell_a_joke():
    joke = random.choice(jokes)
    return flask.render_template('joke.html', joke_text=joke)
