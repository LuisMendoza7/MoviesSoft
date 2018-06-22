from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/luis/PyEx/FlaskProjects/MoviesSoft/movies.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), unique = True, nullable = False)
    password = db.Column(db.String(50), unique = False, nullable = False)
    type = db.Column(db.String(20), unique = False, nullable = False)
    avatar = db.Column(db.String(50), unique = True, nullable = True)

    def __repr__(self):
        return '<User: %r>' % self.username

###############################################################################

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    moviename = db.Column(db.String(50), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    director = db.Column(db.String(50), unique=False, nullable=False)
    distributor = db.Column(db.String(50), unique=False, nullable=False)
    description = db.Column(db.String(500), unique=False, nullable=True)
    image = db.Column(db.String(50), unique=True, nullable=True)

    def __repr__(self):
        return '<Movie: %r>' % self.moviename
