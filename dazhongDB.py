import time,random,ssl
from urllib import request
from urllib.parse import quote
from bs4 import BeautifulSoup
import mongo as db


def reduceSame(vl):
    arr=[]
    for id in vl:
        if id not in arr:
            arr.append(id)
    return arr

def reqst(str, fg, count):
    if fg==1:
        req = request.Request(quote(str, safe='/:?='))
    else:
        req = request.Request(str)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')
    with request.urlopen(req) as response:
        html = response.read().decode("utf-8")

    bs = BeautifulSoup(html, "html.parser")
    dd = bs.find_all(name='div',attrs={"class":"txt"})
    ee = bs.find_all(name='div', attrs={"class": "comment"})
    ff = bs.find_all(name='span',attrs={"class":"addr"})
    gg = bs.find_all(name='a',attrs={"class":"mean-price"})

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
    c=bs.find(name='a', attrs={"class": "next"})

    try:
        time.sleep(random.randint(0, 1000) * 0.001)
        print("已完成第%i页数据添加"%count)
        count=count+1
        reqst(c.get('href'),0,count)
    except AttributeError as e:
        db.insert(vl)
        db.find()

ssl._create_default_https_context = ssl._create_unverified_context
str="http://www.dianping.com/search/keyword/3/0_mamala"
vl = []
reqst(str,1,1)