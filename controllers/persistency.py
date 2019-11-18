"""
Persistency functions
"""
from flask import current_app

def save_user(user):
    db = current_app.config['DB_CONNECTION']
    result = db.users.insert_one(user)
    return result

def get_user(user_id):
    db = current_app.config['DB_CONNECTION']
    db_index = {
        "_id": user_id
    }
    result = db.users.find_one(db_index)
    return result
