from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    app.mongo = MongoClient(app.config["MONGO_URI"])
    from .routes import main
    app.register_blueprint(main)
    return app
