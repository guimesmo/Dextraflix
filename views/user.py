from flask import Blueprint, request, make_response, current_app
from flask import g
user_bp = Blueprint(name="user", import_name="user")

@user_bp.route('/user', methods=['POST'])
def post_user():
    print("Creating new user")
    user_schema = current_app.config["USER_SCHEMA"]
    db = current_app.config["PERSISTENCY"]
    results = user_schema.validate(request.json)
    if results.keys():
        make_response(f'{results}', 400)
    else:
        print("Adding to mongo")
        db.save_user(request.json)
        return make_response('teste', 200)