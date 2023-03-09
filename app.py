from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story
from stories import excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

foo = [silly_story, excited_story]


@app.get("/questions")
def generate_madlib_form():
    """Generates an html form given the prompts from `silly_story`."""
    response = request.args["story"]
    for story in foo:
        if story.name == response:
            found = story


    return render_template("questions.html", words=found.prompts, n=found.name)


@app.get("/results")
def display_madlib_result():
    """Given user form data, fill in their madlib and show it."""

    response = request.args
    delete_name = response.pop("name")
    for story in foo:
        if story.name == delete_name:
            found = story

    story = found.generate(response)
    return render_template("results.html", story_out=story)

@app.get("/home")
def display_story_templates():
    """Generates a drop down menu of story templates"""

    names = [n.name for n in foo]

    return render_template("dropdown.html", story_template=names)





