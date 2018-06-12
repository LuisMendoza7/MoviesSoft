import os
from flask import Flask, request, render_template, url_for, redirect, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug import secure_filename

app = Flask("Movies DataBase")
# app = Flask("Movies DataBase", static_folder="images")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/luis/PyEx/FlaskProjects/MoviesSoft/movies.db'
db = SQLAlchemy(app)

UPLOAD_FOLDER = '/home/luis/PyEx/FlaskProjects/MoviesSoft/static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    moviename = db.Column(db.String(50), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=True, nullable=False)
    director = db.Column(db.String(50), unique=True, nullable=False)
    image = db.Column(db.String(50), unique=True, nullable=True)

    def __repr__(self):
        return '<Movie: %r>' % self.moviename

def show_movies():
    movies_list = Movies.query.all()
    if len(movies_list) == 0:
        return 'There are no movies in the database.'
    return movies_list

def add_movie(*args):
    movie = Movies(moviename=args[0], year=args[1], director=args[2], image=args[3])
    db.session.add(movie)
    db.session.commit()

def delete_movie(*args):
    id = args[0]
    Movies.query.filter(Movies.id == id).delete()
    db.session.commit()

def select_movie(*args):
    id = args[0]
    movie = Movies.query.filter_by(id = id).first()
    return movie

def modify_movie(*args):
    id = args[0]
    name = args[1]
    year = args[2]
    director = args[3]

    movie = Movies.query.filter_by(id = id).first()

    movie.moviename = name
    movie.year = year
    movie.director = director
    db.session.commit()



###############################################################################
@app.route('/')

def index():
    return redirect(url_for('home'))

###############################################################################

@app.route('/home', methods=['GET'])
def home():
    if type(show_movies()) == str:
        show_message = True
        movies = show_movies()
        return render_template('home.html', show_message=show_message, movies=movies)

    show_message = False
    movies = show_movies()
    return render_template('home.html', show_message=show_message, movies=movies)

###############################################################################

@app.route('/show', methods=['GET'])
def show():
    if request.method == 'GET':
        if type(show_movies()) == str:
            show_message = True
            movies = show_movies()
            return render_template('show.html', show_message=show_message, movies=movies, active="active")

        show_message = False
        movies = show_movies()
        return render_template('show.html', show_message=show_message, movies=movies, active="active")

###############################################################################

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        if (request.form['name'] == '') or (request.form['year'] == '') or (request.form['director'] == ''):
            message = "You can leave any empty field."
            return render_template('add.html', message = message)

        file = request.files['image']
        filename = secure_filename(file.filename)
        add_movie(request.form['name'], request.form['year'], request.form['director'], filename)
        message = "Registered: %s" % (request.form['name'])
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return render_template('add.html', message=message)

    return render_template('add.html')

###############################################################################

@app.route('/delete/<id>')
def delete(id):
    delete_movie(id)
    message = "Movie deleted."

    if type(show_movies()) == str:
        show_message = True
        movies = show_movies()
        return render_template('show.html', show_message=show_message, movies=movies, message=message)

    show_message = False
    movies = show_movies()
    return render_template('show.html', show_message=show_message, movies=movies, message=message)

###############################################################################

@app.route('/modify/<id>', methods=['GET','POST'])
def modify(id):
    if request.method == 'POST':
        modify_movie(request.form['id'], request.form['name'], request.form['year'], request.form['director'])
        message = "Movie modified."
        movie = select_movie(request.form['id'])
        return render_template('modify.html', movie=movie, message=message)

    movie = select_movie(id)
    return render_template('modify.html', movie=movie)

###############################################################################

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

###############################################################################
app.run(debug=True)
