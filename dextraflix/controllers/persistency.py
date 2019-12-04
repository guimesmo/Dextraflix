"""
Persistency functions
"""
from flask import current_app

def save_user(user):
    db = current_app.config['DB_CONNECTION']
    result = db.users.insert_one(user)
    return result

def update_user(userid, user):
    db = current_app.config['DB_CONNECTION']
    result = db.users.find_one_and_update({"_id": userid}, {"$set": user})
    return result


def get_user(user_id):
    db = current_app.config['DB_CONNECTION']
    db_index = {
        "_id": user_id
    }
    result = db.users.find_one(db_index)
    return result

def delete_user(user_id):
    db = current_app.config['DB_CONNECTION']
    db_index = {
        "_id": user_id
    }
    result = db.users.delete_one(db_index)
    return result
