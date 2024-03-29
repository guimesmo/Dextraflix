from logging import log
from flask import Blueprint, request, make_response, current_app
import uuid
user_bp = Blueprint(name="user", import_name="user")

@user_bp.route('/user', methods=['POST'])
def add_user():
    log = current_app.config["LOGGER"]
    user_schema = current_app.config["USER_SCHEMA"]
    db = current_app.config["PERSISTENCY"]
    log.debug("Creating new user")
    results = user_schema.validate(request.json)
    if results.keys():
        return make_response(results, 400)
    else:
        user_data = request.json
        user_data["_id"] = str(uuid.uuid4())
        db.save_user(user_data)
        msg = {
            "message": "user added",
            "id": user_data["_id"]
        }
        return make_response(msg, 200)

@user_bp.route('/user/<userid>', methods=['GET'])
def get_user(userid):
    log = current_app.config["LOGGER"]
    log.debug(f"Retrieving user {userid}")
    db = current_app.config["PERSISTENCY"]

    user = db.get_user(userid)
    if user:
        return make_response(user, 200)
    else:
        return make_response('user not found', 404)

@user_bp.route('/user/<userid>', methods=['PUT'])
def update_user(userid):
    log = current_app.config["LOGGER"]
    log.debug("Updating user")
    user_schema = current_app.config["USER_SCHEMA"]
    db = current_app.config["PERSISTENCY"]
    results = user_schema.validate(request.json)
    if results.keys():
        return make_response(results, 400)
    else:
        user_data = request.json
        user_data["_id"] = userid
        db.update_user(userid, user_data)
        msg = {
            "message": "user updated",
            "id": user_data["_id"]
        }
        return make_response(msg, 200)


@user_bp.route('/user/<userid>', methods=['DELETE'])
def delete_user(userid):
    log = current_app.config["LOGGER"]
    log.debug(f"Removing user {userid}")
    db = current_app.config["PERSISTENCY"]

    delete_result = db.delete_user(userid)
    
    if delete_result.deleted_count == 1:
        return make_response({"message": "user deleted", "id": userid}, 200)
    else:
        return make_response('user not found', 404)
