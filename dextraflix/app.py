from flask import Flask, g
from flask_pymongo import PyMongo
from dextraflix.views.categoria import categorias_bp
from dextraflix.views.video import videos_bp
from dextraflix.views.user import user_bp
from dextraflix.controllers import get_persistency
import os

# Logging stuff
import logging
logging.basicConfig()

if __name__ == "__main__":
    app = Flask("dextraflix-app")
    with app.app_context():
        app.register_blueprint(videos_bp, url_prefix="/videos")
        app.register_blueprint(categorias_bp, url_prefix="/categories")
        app.register_blueprint(user_bp, url_prefix="/users")
        app.config["MONGO_URI"] = os.environ['MONGO_URI']
        app.config["DB_CONNECTION"] = PyMongo(app).db
        app.config["PERSISTENCY"] = get_persistency
        log = logging.getLogger("dextraflix")
        log.setLevel(logging.DEBUG)
        app.config["LOGGER"] = log
    app.run(host='0.0.0.0')
