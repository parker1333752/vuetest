from flask_sqlalchemy import SQLAlchemy
import models
from new import classobj

DB_URL = 'mysql://sijunli:12345678@localhost/sijunli'


def getAllTables(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db = SQLAlchemy(app)

    Tables = {}
    for i in models.__dict__.iteritems():
        if type(i[1]) is classobj and i[0][-5:] == 'Model':
            tablename = i[0][:-5]
            Tables[tablename] = type(tablename, (db.Model,), i[1].__dict__)
            # Tables[tablename] = type(tablename, (), i[1].__dict__)

    return (db, type("Tables", (), Tables))
