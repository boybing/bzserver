from  pymongo  import  MongoClient
import os

def insert(dblink,data):
        client = MongoClient(dblink)
        db= client.bzbz.dazhong
        print(db.insert(data))

def find(dblink):
        client = MongoClient(dblink)
        db= client.bzbz.dazhong
        for i in db.find():
            print(i)

def remove(dblink):
        type=input("delet all?y or n")
        if type is 'y':
                client = MongoClient(dblink)
                db = client.bzbz.dazhong
                db.remove()
        else:
                pass

# for i in db.find():
#         print(i)
