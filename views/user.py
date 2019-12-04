from logging import log
from flask_restful import Resource, Api
from flask import Blueprint, request, make_response, current_app
import uuid

from models import user_schema

user_bp = Blueprint(name="user", import_name="user")
api = Api(user_bp)

class UserResource(Resource):
    def get(self, userid):
        log = current_app.config["LOGGER"]
        log.debug(f"Retrieving user {userid}")
        db = current_app.config["PERSISTENCY"]

        user = db.get_user(userid)
        if user:
            return user, 200
        else:
            return "user not found", 404
    def put(self, userid):
        log = current_app.config["LOGGER"]
        log.debug("Updating user")
        db = current_app.config["PERSISTENCY"]
        results = user_schema.validate(request.json)
        if results.keys():
            return results, 400
        else:
            user_data = request.json
            user_data["_id"] = userid
            db.update_user(userid, user_data)
            msg = {
                "message": "user updated",
                "id": user_data["_id"]
            }
            return msg, 200

    def delete(self, userid):
        log = current_app.config["LOGGER"]
        log.debug(f"Removing user {userid}")
        db = current_app.config["PERSISTENCY"]

        delete_result = db.delete_user(userid)
        
        if delete_result.deleted_count == 1:
            return {"message": "user deleted", "id": userid}, 200
        else:
            return 'user not found', 404

class UserListResource(Resource):
    def post(self):
        log = current_app.config["LOGGER"]
        # user_schema = current_app.config["USER_SCHEMA"]
        db = current_app.config["PERSISTENCY"]
        log.debug("Creating new user")
        results = user_schema.validate(request.json)
        if results.keys():
            return results, 400
        else:
            user_data = request.json
            user_data["_id"] = str(uuid.uuid4())
            db.save_user(user_data)
            msg = {
                "message": "user added",
                "id": user_data["_id"]
            }
            return msg, 200

api.add_resource(UserResource, '/<string:userid>')
api.add_resource(UserListResource, '/')
