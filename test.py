from flask import Flask
import database

app = Flask(__name__)
(db, Tables) = database.getAllTables(app)

db.create_all()
# db.drop_all()
