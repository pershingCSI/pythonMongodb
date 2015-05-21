#encoding=utf-8
from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

#client = MongoClient('localhost',27017)
client = MongoClient('mongodb://localhost:27017/')

#連接db
# db = client['mydb']
db = client.mydb

#連接collection
# users = db['users']
users = db.users
authors = db.authors

#list all of collections
show_collection_name = db.collection_names(include_system_collections=False)
print show_collection_name

print "------------------------------"

#插入一筆資料，使用insert_one()
# user = {"name":"Mary","gender":"Female"}
# post = users.insert_one(user)

#查詢一筆資料，使用find_one()
print users.find_one()

post1 = users.find_one({'gender':'Female'})
gender = post1['gender']
id = post1['_id']
name = post1['name']
print gender, id, name 

post_id = ObjectId("554ee935f0a962b9a2063869")
post2 = users.find_one({"_id":post_id})
print post2

print "------------------------------"

#一次輸入多筆資，使用find_many()
author = [{"author": "Mike",
            "text": "Another post!",
            "tags": ["bulk", "insert"],
            "date": datetime.datetime(2009, 11, 12, 11, 14)},
           {"author": "Eliot",
            "title": "MongoDB is fun",
            "text": "and pretty easy too!",
            "date": datetime.datetime(2009, 11, 10, 10, 45)}]
new_posts = authors.insert_many(author)


#列出所有資料
for post in authors.find():
	print post




#參考http://api.mongodb.org/python/current/tutorial.html