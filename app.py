from flask import Flask
from pymongo import MongoClient

from routes.user_routes import user
from routes.transaction_routes import transactions
from routes.analytics_routes import analytics

def create_app():
    app = Flask(__name__)
    client = MongoClient('localhost', 27017)
    
    app.register_blueprint(user)
    app.register_blueprint(transactions)
    app.register_blueprint(analytics)
    @app.route('/')
    def index():
        return 'Hello, World!'
    
    return app

