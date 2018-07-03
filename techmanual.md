# Technical Manual
### Index

#### 1. Explanation
This website was developed using Flask, Python, HTML, CSS and other Flask extensions. The website is a movie database where you can upload, modify, delete and see all registers with pictures and descriptions.

##### 1.1 Flask
Flask is a framework that allows you to create and develop web pages with python code. As templates, flask uses Jinja to create a HTML document to show your outputs and messages.

##### 1.2 Python
Python is a programming language based in objects. For this projects, python was used to develop the functions and all logic behind a HTML page.

##### 1.3 HTML & CSS
HTML (HyperText Markup Language) is language to create web pages. HTML use tags to make their document take an appropriate form for it's use.

On the other hand, CSS (Cascading Style Sheets) is a language for graphic designing. It gives it a HTML document, a style for a better show of it's content.

##### 1.4 SQLAlchemy
SQLAlchemy is an object-relational mapper for Python. It creates a database and it's tables using classes, and variables for columns. For this project in particular, SQLAlchemy is used in a database based in SQLite. It stores all all register that are created from the webpage.

#### 2. Requirements and Installation
To run this project, the computer must be executed in a linux operative system. The first requirements are:

- **Python 3.6**
- **Pip (The latest, the better.)**
- **A python virtual environment**
- **A browser**

###### 2.1 Virtual Environment
To create a virtual environment, using a Shell, first create a new folder.
```
mkdir project
cd project
virtualenv -p python3.6 name
```

In your folder **"project"** it will create the a virtual environment folder called **"name"**, the name of the virtual environment can be anyone, just be sure to activate the same you have created.

To activate the virtual environment, you have to type:
```
source name/bin/activate
```

And the prompt will show the name of the virtual environment.

To deactivate just type:

```
deactivate
```

##### 2.2 Automated Installation
Once met those previous requirements, you need to execute your virtual environment and install the next packages. These are stored in a text file called **requirements.txt**, in a shell of your preference, you have to type:
```
pip install -r requirements.txt
```

##### 2.3 Manual Installation
If the **requirements.txt** file is not found, you can install manually all requirements.

###### 2.3.1 Flask
To install Flask, once you have activated your virtual environment, type the next code:
```
pip install Flask
```

Then the shell have ended the installation, flask is ready for it's use.

###### 2.3.2 SQLAlchemy
The installation of SQLAlchemy is easy, just type:
```
pip install Flask-SQLAlchemy
```

#### 3. Endpoints
The URL is `127.0.0.1:5000` for a better use, in the next table just the pages and methods will be show.

|      URL     |        Method        |           Description         |
|    :-----:   |       :-------:      |          :-----------:        |
|   URL/       |        anyone        |      Redirect to URL/main     |
|URL/main      |        None          |    Show login and register    |
| URL/home     |        GET           |        Show all movies        |
| URL/add      |        GET           |     Display add movie page    |
| URL/add      |        POST          |      Register a new movie     |
| URL/movie/*  |        GET           |     Show the movie details    |
| URL/show     |        GET           |   Show all movies in a list   |
| URL/show     |        POST          |    Delete a selected movie    |
| URL/modify/* |        GET           |  Show a movie and modify page |
| URL/modify/* |        POST          | Modify movie and redirect to show |

#### 4. Execute the project
To start the project, locate your shell in the folder, and activate your virtual environment:
```
cd project
source virtualenv/bin/activate
```

Then execute the application:
```
python movies.py
```
![img1](/docs/img1.png)
Once you see those messages in your shell, you are ready to use the project.
