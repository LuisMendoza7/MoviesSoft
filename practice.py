from flask import Flask, render_template, redirect, abort, url_for
from flask import make_response
app = Flask(__name__)


dict = {"Name": "Luis", "Age": 22}

@app.route('/', methods=['GET'])
def hello():
    return redirect(url_for('index'))

@app.route('/index', methods=['GET'])
def index():
    # abort(401)       Unauthorized page, aborts execution of below code.
    return render_template('template.html', dict=dict)



# Customizable 404 error
# @app.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404


# @app.errorhandler(404)
# def not_found(error):
#     resp = make_response(render_template('404.html'), 404)
#     resp.headers['Content-type'] = 'application/json'
#     return resp
#     # return render_template('404.html'), 404


app.run(debug=True)
