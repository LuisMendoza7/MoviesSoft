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

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

###############################################################################

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

###############################################################################

def file_extension(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

###############################################################################

def show_movies():
    movies_list = Movies.query.all()
    if len(movies_list) == 0:
        return 'Database empty.'
    return movies_list

###############################################################################

def add_movie(*args):
    if len(args) == 6:
        movie = Movies(moviename=args[0], year=args[1], director=args[2], distributor=args[3], description=args[4],image=args[5])
        db.session.add(movie)
        db.session.commit()
        return "Added: %s" % args[0]

    movie = Movies(moviename=args[0], year=args[1], director=args[2], distributor=args[3], description=args[4])
    db.session.add(movie)
    db.session.commit()
    return "Added: %s" % args[0]

###############################################################################

# def add_user(*args):
#     user = Users(username=args[0], password=args[1])
#     db.session.add(user)
#     db.session.commit()

###############################################################################

def delete_movie(*args):
    id = args[0]
    Movies.query.filter(Movies.id == id).delete()
    db.session.commit()

###############################################################################

def select_movie(*args):
    id = args[0]
    movie = Movies.query.filter_by(id = id).first()
    return movie

###############################################################################

def modify_movie(*args):
    id = args[0]

    if len(args) == 7:
        movie = Movies.query.filter_by(id = id).first()
        movie.moviename = args[1]
        movie.year = args[2]
        movie.director = args[3]
        movie.description = args[3]
        movie.distributor = args[4]
        movie.image = args[6]
        db.session.commit()
        return "Movie Modified"

    movie = Movies.query.filter_by(id = id).first()
    movie.moviename = args[1]
    movie.year = args[2]
    movie.director = args[3]
    movie.distributor = args[4]
    movie.description = args[5]
    db.session.commit()
    return "Movie Modified."



###############################################################################
@app.route('/')
def index():
    return redirect(url_for('main'))

###############################################################################

@app.route('/main')
def main():
    return render_template('main.html')

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

@app.route('/movie/<id>', methods=['GET'])
def detailed_movie(id):
    movie = select_movie(id)
    return render_template('detail.html', movie=movie)


###############################################################################

@app.route('/show', methods=['GET'])
def show():
    if request.method == 'GET':
        if type(show_movies()) == str:
            show_message = True
            movies = show_movies()
            return render_template('show.html', show_message=show_message, movies=movies)

        show_message = False
        movies = show_movies()
        return render_template('show.html', show_message=show_message, movies=movies)

###############################################################################

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':

        if (request.form['name'] == '') or (request.form['year'] == '') or (request.form['director'] == '') or (request.form['distributor'] == ''):
            message = "You can not leave any empty field."
            show_message = True
            return render_template('add.html', message = message, show_message=show_message)

        if request.form['year'].isalpha():
            message = "Year field must be a number."
            show_message = True
            return render_template('add.html', message = message, show_message=show_message)

        try:
            file = request.files['image']
            filename = secure_filename(file.filename)
            if file_extension(filename):
                if type(show_movies()) == str:
                    extension = filename.split('.')[1]
                    imagename = "image0."+extension
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], imagename))
                    add_movie(request.form['name'], request.form['year'], request.form['director'], request.form['distributor'], request.form['description'], imagename)
                    message = "Registered: %s" % (request.form['name'])
                    show_message = True
                    return render_template('add.html', message=message, show_message=show_message)

                extension = filename.split('.')[1]
                imagename = "image"+str(len(show_movies()))+"."+extension
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], imagename))
                add_movie(request.form['name'], request.form['year'], request.form['director'], request.form['distributor'], request.form['description'], imagename)
                message = "Registered: %s" % (request.form['name'])
                show_message = True
                return render_template('add.html', message=message, show_message=show_message)

            message = "Upload a jpeg, jpg or png image."
            show_message = True
            return render_template('add.html', message=message, show_message=show_message)

        except:
            add_movie(request.form['name'], request.form['year'], request.form['director'], request.form['distributor'], request.form['description'])
            message = "Registered: %s" % (request.form['name'])
            show_message = True
            return render_template('add.html', message=message, show_message=show_message)

    return render_template('add.html')

###############################################################################

@app.route('/delete/<id>')
def delete(id):

    filename = select_movie(id).image
    name = select_movie(id).moviename
    if filename:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        delete_movie(id)
        message = "Deleted: %s" % name

    delete_movie(id)
    message = "Deleted: %s" % name

    if type(show_movies()) == str:
        show_message = True
        movies = show_movies()
        return render_template('show.html', show_message=show_message, movies=movies)

    show_message = False
    movies = show_movies()
    return render_template('show.html', show_message=show_message, movies=movies, message=message)

###############################################################################

@app.route('/modify/<id>', methods=['GET', 'POST'])
def modify(id):
    if request.method == 'POST':
        try:
            file = request.files['image']
            oldfilename = select_movie(request.form['movieid']).image
            newfilename = secure_filename(file.filename)
            if oldfilename:
                if oldfilename != newfilename:
                    extension = newfilename.split('.')[1]
                    imagename = "image"+str(len(show_movies()))+"."+extension
                    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], oldfilename))
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], imagename))
                    message = modify_movie(request.form['movieid'], request.form['name'], request.form['year'], request.form['director'], request.form['distributor'], request.form['description'], imagename)
                    movies = show_movies()
                    return render_template('show.html', movies=movies, message=message)

                message = "You can not upload an image with the same name."
                return render_template('show.html', movies=movies, message=message)

            extension = newfilename.split('.')[1]
            imagename = "image"+str(len(show_movies()))+"."+extension
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], imagename))
            modify_movie(request.form['movieid'], request.form['name'], request.form['year'], request.form['director'], request.form['distributor'], request.form['description'], imagename)
            return redirect(url_for('show'))

        except:
            modify_movie(request.form['movieid'], request.form['name'], request.form['year'], request.form['director'], request.form['distributor'], request.form['description'])
            return redirect(url_for('show'))

    movie = select_movie(id)
    return render_template('modify.html', movie=movie)

###############################################################################

# @app.route('/register', methods=['POST'])
# def register():
#     if request.method == 'POST':
#         pass

###############################################################################

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

###############################################################################
app.run(debug=True)
