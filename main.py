from flask import Flask
from flask_pymongo import PyMongo
from Dextraflix.views.categoria import categorias_bp
from Dextraflix.views.video import videos_bp

app = Flask(__name__)

app.register_blueprint(videos_bp)
app.register_blueprint(categorias_bp)

app.config["MONGO_URI"] = "mongodb://localhost:27017/dextraflix"
mongo = PyMongo(app)
