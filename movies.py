from flask import Flask, request, jsonify, render_template, url_for, redirect
app = Flask("Movies DataBase")

class Movies:
    def __init__(self):
        self.movies_list = []

    def add_movie(self, *args):
        if len(self.movies_list) > 0:
            movie_exists = list(filter(lambda key: key["Name"] == args[0], self.movies_list))
            if len(movie_exists) > 0:
                return "That movie already exists."

            movie = {"Name": args[0], "Year": args[1], "Director": args[2]}
            self.movies_list.append(movie)
            return "Movie added."

        movie = {"Name": args[0], "Year": args[1], "Director": args[2]}
        self.movies_list.append(movie)
        return "Movie added."


    def show_movies(self):
        if len(self.movies_list) == 0:
            return "There are no movies in the database."
        return self.movies_list

    def delete_movie(self, *args):
        new_movies = [movie for movie in self.movies_list if movie["Name"] != args[0]]
        self.movies_list = new_movies

    def movie_check(self, *args):
        movie_exists = list(filter(lambda key: key["Name"] == args[0], self.movies_list))
        print (args[0])
        print (movie_exists)
        if len(self.movies_list) == 0:
            return None
        if len(movie_exists) == 0:
            return False
        return True

    def modify_movie(self, *args):
        id = args[0]
        name = args[1]
        year = args[2]
        director = args[3]
        if self.movie_check(id) == None:
            return "There are no movies in the database."
        elif self.movie_check(id) == False:
            return "That movie does not exists."
        elif self.movie_check(id) == True:
            update_movie = next(movie for movie in self.movies_list if movie['Name'] == id)
            if (name == '') and (year == '') and (director == ''):
                return "No changes have been made."
            if name != '':
                update_movie['Name'] = name
            if year != '':
                update_movie['Year'] = year
            if director != '':
                update_movie['Director'] = director
            return "Movie Updated!"

movies_db = Movies()
###############################################################################
@app.route('/')

def index():
    return redirect(url_for('home'))

###############################################################################

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

###############################################################################

@app.route('/show', methods=['GET'])
def show():
    if request.method == 'GET':
        if type(movies_db.show_movies()) == str:
            movies = movies_db.show_movies()
            show_message = True
            return render_template('show.html', movies = movies, show_message = show_message)

        movies = movies_db.show_movies()
        show_message = False
        return render_template('show.html', movies = movies, show_message = show_message)



###############################################################################

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        movies_db.add_movie(request.form['name'], request.form['year'], request.form['director'])
        message = "Added: %s" % (request.form['name'])
        return redirect(url_for('show', message = message))

    return render_template('add.html')


###############################################################################

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        if movies_db.movie_check(request.form['name']) == None:
            message = "There are not movies in the database."
            return redirect(url_for('show', message = message))

        elif movies_db.movie_check(request.form['name']) == False:
            message = "That movie does not exists."
            return redirect(url_for('show', message = message))

        elif movies_db.movie_check(request.form['name']) == True:
            movies_db.delete_movie(request.form['name'])
            message = "Movie deleted: %s" % (request.form['name'])
            if len(movies_db.movies_list) == 0:
                return redirect(url_for('show'))
            return redirect(url_for('show', message = message))

###############################################################################

@app.route('/modify', methods=['POST'])
def modify():
    if request.method == 'POST':
        movies_db.modify_movie(request.form['moviename'], request.form['name'], request.form['year'], request.form['director'])
        message = "Modified: %s" % (request.form['moviename'])
        return redirect(url_for('show', message = message))

###############################################################################

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

###############################################################################
app.run(debug=True)
