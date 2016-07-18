from flask import Flask
from flask import render_template
import models

app = Flask(__name__)
DB_URL = 'mysql://sijunli:12345678@localhost/sijunli'

(db, Tables) = models.getAllTables(app, DB_URL)
# db.create_all()
# db.drop_all()


@app.route("/")
def test():
    return render_template("test.html")

app.run("0.0.0.0", 1315)
