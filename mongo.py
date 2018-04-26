from  pymongo  import  MongoClient

def insert(data):
        client = MongoClient("mongodb://bingzai:bingzai@ds255319.mlab.com:55319/bzbz")
        db= client.bzbz.dazhong
        print(db.insert(data))

def find():
        client = MongoClient("mongodb://bingzai:bingzai@ds255319.mlab.com:55319/bzbz")
        db= client.bzbz.dazhong
        for i in db.find():
            print(i)

def remove():
        type=input("delet all?y or n")
        if type is 'y':
                client = MongoClient("mongodb://bingzai:bingzai@ds255319.mlab.com:55319/bzbz")
                db = client.bzbz.dazhong
                db.remove()
        else:
                pass

# for i in db.find():
#         print(i)
