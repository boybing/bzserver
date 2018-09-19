"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import dazhongdianpin as dz
import os
import mongo
import time
import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')
# app.config['DDDD']=os.environ['DDDD']
# app.config['DB_LINK']=os.environ['DB_LINK']

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    # mongo.insert(app.config['DB_LINK'],[{'xx':'xx'}])

    return "Hello World !".encode()

@app.route('/d/<id>')
def ariticle(id):
    # dz.dblink=app.config['DB_LINK']
    # dz.dazhongdianpin('',id)
    # f = open(r'test.txt', 'r')  # 打开所保存的cookies内容文件
    cookies = {}  # 初始化cookies字典变量
    for line in '_lxsdk_cuid=162dd1afa327c-0adaa32fabe195-33697b04-fa000-162dd1afa33c8; _lxsdk=162dd1afa327c-0adaa32fabe195-33697b04-fa000-162dd1afa33c8; _hc.v=b6a8900b-a829-9d67-3821-69ad020e7290.1524127956; s_ViewType=10; ua=dpuser_8775393991; ctu=fd0193bb6215b37ebea4235d05b07e6d84c24619e199b41fa00b2b816b5cecdf; UM_distinctid=162dd2447d7480-0479774a4488e6-33697b04-fa000-162dd2447d8b53; aburl=1; QRCodeBottomSlide=hasShown; cy=3; cye=hangzhou; ctu=3219540c83f3acb32b2ffdf8de65df8dc294f04f715c1d427b2a30caac0a5a195cf74e7ebbda8e66ac1526b4b2812fb7; _lxsdk_s=16367f63de6-505-aa0-a5a%7C%7C38'.split(';'):  # 按照字符：进行划分读取
        # 其设置为1就会把字符串拆分成2份
        name, value = line.strip().split('=', 1)
        cookies[name] = value  # 为字典cookies添加内容

    session=requests.session()
    headers = {'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
    r = session.get(url= 'https://www.dianping.com',headers=headers)
    resp=session.get(url='http://www.dianping.com/search/keyword/3/0_%E4%B8%87%E8%B1%A1%E5%9F%8E',headers=headers)
    print(r.request.headers)
    print(r.headers)
    print(r.cookies)
    print(r.status_code)
    print(resp.request.headers)
    print(resp.headers)
    print(resp.cookies)
    print(resp.status_code)
    html=resp.text
    print(html)

    bs = BeautifulSoup(html, "html.parser")
    dd = bs.find_all(name='div', attrs={"class": "txt"})
    ee = bs.find_all(name='div', attrs={"class": "comment"})
    ff = bs.find_all(name='span', attrs={"class": "addr"})
    gg = bs.find_all(name='a', attrs={"class": "mean-price"})
    vl=[]
    for i in range(len(gg)):
        try:
            if gg[i].b is None:
                vl.append({'title': dd[i].a.h4.string, 'price': "￥0", 'stars': ee[i].span.get('title'),
                           'address': ff[i].string, "review": ee[i].a.b.string,"url":dd[i].a.get('href'),"time":time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))})
            else:
                vl.append({'title': dd[i].a.h4.string, 'price': gg[i].b.string, 'stars': ee[i].span.get('title'),
                           'address': ff[i].string, "review": ee[i].a.b.string,"url":dd[i].a.get('href'),"time":time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))})
        except:
            vl.append({'title': dd[i].a.h4.string, 'price': "￥0", 'stars': ee[i].span.get('title'),
                       'address': ff[i].string, "review": "0","url":dd[i].a.get('href'),"time":time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))})
    print(vl)
    return html


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


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
