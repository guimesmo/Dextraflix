from flask import Flask, g
from flask_pymongo import PyMongo
from views.categoria import categorias_bp
from views.video import videos_bp
from views.user import user_bp
from controllers import persistency

# Logging stuff
import logging
logging.basicConfig()

app = Flask(__name__)
with app.app_context():
    app.register_blueprint(videos_bp)
    app.register_blueprint(categorias_bp)
    app.register_blueprint(user_bp, url_prefix="/users")
    app.config["MONGO_URI"] = "mongodb://localhost:27017/dextraflix"
    db = PyMongo(app).db
    app.config["DB_CONNECTION"] = db
    app.config["PERSISTENCY"] = persistency
    log = logging.getLogger("dextraflix")
    log.setLevel(logging.DEBUG)
    app.config["LOGGER"] = log


if __name__ == '__main__':    
    app.run(host='0.0.0.0')

