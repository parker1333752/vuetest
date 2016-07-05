from flask import Flask
from flask import render_template
from flask import redirect

app = Flask(__name__)


@app.route("/")
def test():
    return render_template("test.html")

#app.run("0.0.0.0", 1315)

from database import init
init(app)
import database
