# python library code
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
#define user authentication
    def __init__(self,username,password):
        self.client = MongoClient('mongodb://localhost:47778')
        self.database = self.client['AAC']        
# define create method
    def create(self, data):
        # Checks to see if the data is null or empty and returns false in either case
        if data is not None:
            self.database.animals.insert_one(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")  
            
    def read_all(self,data):
        cursor = self.database.animals.find(data, {'_id':False})
        return cursor
    
#define read method
    def read(self, search):
        # Checks to see if the data is null or empty and returns exception in either case
        if search is not None:
            if search:
                searchResult = self.database.animals.find(search)
                return searchResult
        else:
            raise Exception("Nothing to search, because data parameter is empty")
            
#define update method
    def update(self, data, newData):
        if data is not None:
            updated = self.database.animals.update_many(data, newData)
            return dumps(self.read(newData))
        else:
            raise Exception("Nothing to update, because data parameter is empty")
            
#define delete method
    def delete(self, data):
        if data is not None:
            deleted = self.database.animals.delete_many(data)
            return dumps(self.read(data))
        else:
            raise Exception("Nothing to delete, because data parameter is empty")