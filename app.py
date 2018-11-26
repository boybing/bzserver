"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
import mongo
import requests

from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')
app.config['JSON_AS_ASCII'] = False


# app.config['DDDD']=os.environ['DDDD']
# app.config['DB_LINK']=os.environ['DB_LINK']

###
# Routing for your application.
###

def getBeijinTime():
    try:
        r = requests.get('http://quan.suning.com/getSysTime.do')
        if r.status_code == 200:
            return r.text
        else:
            return "获取时间失败"

    except:
        return "获取时间失败"


@app.route('/', methods=['GET', 'POST'])
def home():
    """Render website's home page."""
    # print(getBeijinTime())
    # tm=getBeijinTime()
    # mongo.insert(app.config['DB_LINK'], [{'time': tm}])
    return "hello world!"


###
# The functions below should be applicable to all Flask apps.
###

# @app.route('/<file_name>.txt')
# def send_text_file(file_name):
#     """Send your static text file."""
#     file_dot_text = file_name + '.txt'
#     return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
