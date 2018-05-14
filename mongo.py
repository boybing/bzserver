from  pymongo  import  MongoClient
import os

def insert(data):
        client = MongoClient(os.environ.get['DB_LINK'])
        db= client.bzbz.dazhong
        print(db.insert(data))

def find():
        client = MongoClient(os.environ.get['DB_LINK'])
        db= client.bzbz.dazhong
        for i in db.find():
            print(i)

def remove():
        type=input("delet all?y or n")
        if type is 'y':
                client = MongoClient(os.environ.get['DB_LINK'])
                db = client.bzbz.dazhong
                db.remove()
        else:
                pass

# for i in db.find():
#         print(i)
