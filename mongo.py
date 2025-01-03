
## Python mongoDB

## What is database? -> place to store data, collection of data can be stored.
## Types of database: SQL, NoSQL

## JSON -> JavaScript Object Notation
{'name': 'John', 'age': 25, 'address': 'New York', 'qualification': {'degree': 'Masters', 'year': 2020}} 

## pymongo -> python module to connect to mongoDB

import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/') # connecting to mongoDB

db = client['mydatabase'] # creating a database

collection = db['students'] # creating a collection

## hierarchy : client -> database -> collection -> document

## basic CRUD operations

## C - Create
## R - Read
## U - Update
## D - Delete

## Create

data = {'name': 'John', 'age': 25, 'address': 'New York', 'qualification': {'degree': 'Masters', 'year': 2020}}

data1 = [
    {'name': 'Smith', 'age': 30, 'address': 'California', 'qualification': {'degree': 'Bachelors', 'year': 2018}},
    {'name': 'David', 'age': 35, 'address': 'Texas', 'qualification': {'degree': 'PhD', 'year': 2022}}
]

try:
    # collection.insert_one(data) # inserting one document
    collection.insert_many(data1)
except Exception as e:
    print('Error in inserting data')
else:
    print('Data inserted successfully')

# Read

result = collection.find_one({"name": "Smith"}) # fetching one document
print(result)


## find()

result = collection.find({"name": "John"}) # fetching all documents
for i in result:
    print(i)   

# Update

collection.update_one({"name": "John"}, {"$set": {"age": 30}}) # updating one document

collection.update_many({"name": "John"}, {"$set": {"age": 30}}) # updating all documents

## Delete

collection.delete_one({"name": "John"}) # deleting one document

collection.delete_many({"name": "John"}) # deleting all documents

# Drop collection

collection.drop()

# Drop database

client.drop_database('mydatabase')

## Queries

## $eq -> equal
## $gt -> greater than
## $lt -> less than
## $gte -> greater than equal to
## $lte -> less than equal to

result = collection.find({"age": {"$gt": 25}}) # fetching all documents where age is greater than 25
for i in result:
    print(i)

collection.update_many({}, {"$set":{'qualification.degree': 'Masters'}}) # updating all documents where qualification is Masters

result = collection.find({"qualification.degree": "Masters"}) # fetching all documents where qualification is Masters
for document in result:
    for key, value in document.items():
        print(f"{key}: {value}")
    print("\n ---------------- \n")


## sort, limit

collection.insert_many([
    {
        "username": "emilyclark",
        "email": "emilyclark@example.com",
        "age": 22,
        "is_active": True,
        "join_date": "2023-01-18",
        "profile": {
            "bio": "Student and aspiring writer.",
            "website": "https://emilywrites.com",
            "location": "Toronto, Canada"
        },
        "hobbies": ["writing", "reading", "painting"]
    },
    {
        "username": "robertbrown",
        "email": "robertbrown@example.com",
        "age": 35,
        "is_active": False,
        "join_date": "2020-07-11",
        "profile": {
            "bio": "Entrepreneur and business consultant.",
            "website": "https://robertbiz.com",
            "location": "Chicago, USA"
        },
        "hobbies": ["consulting", "golfing", "traveling"]
    },
    {
        "username": "lucywilliams",
        "email": "lucywilliams@example.com",
        "age": 27,
        "is_active": True,
        "join_date": "2023-06-05",
        "profile": {
            "bio": "Fitness trainer and health coach.",
            "website": "https://lucyfit.com",
            "location": "Sydney, Australia"
        },
        "hobbies": ["fitness", "cooking", "hiking"]
    },
    {
        "username": "davidharris",
        "email": "davidharris@example.com",
        "age": 29,
        "is_active": True,
        "join_date": "2022-09-20",
        "profile": {
            "bio": "Musician and composer.",
            "website": "https://davidharris.music",
            "location": "Berlin, Germany"
        },
        "hobbies": ["music", "composing", "traveling"]
    },
    {
        "username": "sophiamiller",
        "email": "sophiamiller@example.com",
        "age": 31,
        "is_active": False,
        "join_date": "2021-12-15",
        "profile": {
            "bio": "Graphic designer and illustrator.",
            "website": "https://sophiamiller.design",
            "location": "Paris, France"
        },
        "hobbies": ["designing", "drawing", "photography"]
    },
    {
        "username": "liamjohnson",
        "email": "liamjohnson@example.com",
        "age": 26,
        "is_active": True,
        "join_date": "2023-03-07",
        "profile": {
            "bio": "Blockchain developer and crypto enthusiast.",
            "website": "https://liamcrypto.tech",
            "location": "Singapore"
        },
        "hobbies": ["blockchain", "trading", "reading"]
    },
    {
        "username": "oliviajones",
        "email": "oliviajones@example.com",
        "age": 24,
        "is_active": True,
        "join_date": "2023-08-22",
        "profile": {
            "bio": "Social media influencer and content creator.",
            "website": "https://olivia.social",
            "location": "Los Angeles, USA"
        },
        "hobbies": ["photography", "traveling", "blogging"]
    },
    {
        "username": "ethanwilliams",
        "email": "ethanwilliams@example.com",
        "age": 33,
        "is_active": True,
        "join_date": "2021-10-10",
        "profile": {
            "bio": "Freelance web developer.",
            "website": "https://ethanweb.dev",
            "location": "Dublin, Ireland"
        },
        "hobbies": ["coding", "gaming", "reading"]
    }
]
)

## sort() -> sort the documents based on the given field in ascending or descending order 

result = collection.find().sort("age", -1)

for docs in result:
 
    for key, items in docs.items():

        print(f"{key}: {items}")
 
    print("\n ---------------- \n")


## limit() -> limit the number of documents to be fetched

result = collection.find({"age": {"$gt": 30}}).sort("age", -1).limit(5)

for docs in result:

    for key, values in docs.items():

        print(f"{key}: {values}")

    print("\n---------------------------------\n")

