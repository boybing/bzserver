# coding=utf-8

import mongo
from flask import Flask, render_template, request, jsonify
import hashlib
import json

app = Flask(__name__)

# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')
app.config['DB_LINK']=os.environ['DB_LINK']
app.config['KSTR']=os.environ['KSTR']

###`
# Routing for your application.
###

def get_token(str, token):
    retRes = False
    m1 = hashlib.md5()
    m1.update(str.encode("utf-8"))
    tk = m1.hexdigest()
    if tk == token:
        retRes = True
    print (token)
    print (tk)
    return retRes

# 校对token
def getMd5(time, token):
    try:
        tmpStr = time + app.config['KSTR']
        print (tmpStr)
        return get_token(tmpStr, token)
    except:
        raise RuntimeError('Token错误')


@app.route('/addData', methods=['POST'])
def home():
    """Render website's home page."""
    try:
        jj=json.loads(request.json)
        print jj.get("time")

        if getMd5(jj.get("time"), jj.get("token")):
            mongo.insert(app.config['DB_LINK'], jj)
            return jsonify(code=200, status=0, message='ok')
        else:
            raise RuntimeError("系统错误")
    except:
        return render_template('404.html'), 404


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
    app.run(debug=True)
