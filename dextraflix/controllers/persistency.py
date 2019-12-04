"""
Persistency functions
"""
from flask import current_app

class Persistency:
    def __init__(self, collection):
        self.collection = collection

    def save(self, dict_obj):
        db = current_app.config['DB_CONNECTION']
        result = db[self.collection].insert_one(dict_obj)
        return result

    def update(self, dict_obj_id, dict_obj):
        db = current_app.config['DB_CONNECTION']
        result = db[self.collection].find_one_and_update({"_id": dict_obj_id}, {"$set": dict_obj})
        return result


    def get(self, dict_obj_id):
        db = current_app.config['DB_CONNECTION']
        db_index = {
            "_id": dict_obj_id
        }
        result = db[self.collection].find_one_or_404(db_index)
        return result

    def delete(self, dict_obj_id):
        db = current_app.config['DB_CONNECTION']
        db_index = {
            "_id": dict_obj_id
        }
        result = db[self.collection].delete_one(db_index)
        return result

persistency_cache = {}

def get_persistency(collection):
    if not collection in persistency_cache:
        persistency_cache[collection] = Persistency(collection)
    return persistency_cache[collection]
