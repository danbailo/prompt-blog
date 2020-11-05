import pymongo

#dont need to use __init__ method, because i wont use more than one database,
#its a static and fullstack project

#if i need to use different hosts, and databases, i would to need create more instances of a class
#to handle it, so, i should use __init__

class Database:
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client["fullstack"]

    @staticmethod
    def insert(colletion, data):
        Database.DATABASE[colletion].insert(data)

    @staticmethod
    def find(colletion, query):
        return Database.DATABASE[colletion].insert(query)

    @staticmethod
    def find_one(colletion, query):
        return Database.DATABASE[colletion].insert(query)

