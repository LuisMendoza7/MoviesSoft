from flask import Flask, request, jsonify
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
        return jsonify(self.movies_list)

    def delete_movie(self, *args):
        new_movies = [movie for movie in self.movies_list if movie["Name"] != args[0]]
        self.movies_list = new_movies
        return jsonify(self.movies_list)

    def movie_check(self, *args):
        movie_exists = list(filter(lambda key: key["Name"] == args[0], self.movies_list))
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

@app.route('/movies', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        print (movies_db.add_movie(request.form['name'], request.form['year'], request.form['director']))
        message = movies_db.show_movies()
        return message

    message = movies_db.show_movies()
    return message
###############################################################################

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        if movies_db.movie_check(request.form['name']) == None:
            return "There are no movies in the database."
        elif movies_db.movie_check(request.form['name']) == False:
            return "That movie does not exists."
        elif movies_db.movie_check(request.form['name']) == True:
            message = movies_db.delete_movie(request.form['name'])
            if len(movies_db.movies_list) == 0:
                return "There are no movies in the database."
            return message

    message = movies_db.show_movies()
    return message

###############################################################################

@app.route('/modify', methods=['GET', 'PUT'])
def modify():
    if request.method == 'PUT':
        if request.form['moviename'] == '':
            return "You must select a movie."
        if (request.form['name'] == '') and (request.form['year'] == '') and (request.form['director'] == ''):
            message = movies_db.show_movies()

        print (movies_db.modify_movie(request.form['moviename'], request.form['name'], request.form['year'], request.form['director']))
        message = movies_db.show_movies()
        return message

    message = movies_db.show_movies()
    return message

###############################################################################
app.run(debug=True)
