import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

POSTGRES = {
'user': 'postgres',
'pw': '12345',
'db': 'movies',
'host': 'localhost',
'port': '5432'
}

# DATABASE_URL="sqlite:////home/luis/PyEx/FlaskProjects/MoviesSoft/movies.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

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
    extra = db.Column(db.String(10))

    def __repr__(self):
        return '<Movie: %r>' % self.moviename

manager.run()
