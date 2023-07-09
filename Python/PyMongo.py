from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['MyDB']
collection = db['Student']

document = {'name': 'Atharva', 'age': 23}
result = collection.insert_one(document)
document = {'name': 'Ashutosh', 'age': 22}
result = collection.insert_one(document)

cursor = collection.find()
for document in cursor:
    print(document)

filter = {'name': 'Atharva'}
update = {'$set': {'age': 35}}
result = collection.update_one(filter, update)
print(result.modified_count)

filter = {'name': 'Atharva'}
result = collection.delete_one(filter)
print(result.deleted_count)
