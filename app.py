from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/questions")
def generate_madlib_form():
    """Generates an html form given the prompts from `silly_story`."""

    return render_template("questions.html", words=silly_story.prompts)


@app.get("/results")
def display_madlib_result():
    """Given user form data, fill in their madlib and show it."""
    
    response = request.args
    story = silly_story.generate(response)
    return render_template("results.html", story_out=story)
