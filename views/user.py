from flask import Blueprint, request, make_response, current_app
import uuid
user_bp = Blueprint(name="user", import_name="user")

@user_bp.route('/user', methods=['POST'])
def add_user():
    print("Creating new user")
    user_schema = current_app.config["USER_SCHEMA"]
    db = current_app.config["PERSISTENCY"]
    results = user_schema.validate(request.json)
    if results.keys():
        return make_response(f'{results}', 400)
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
    print(f"Retrieving user {userid}")
    db = current_app.config["PERSISTENCY"]

    user = db.get_user(userid)
    if user:
        return make_response(user, 200)
    else:
        return make_response('user not found', 404)
