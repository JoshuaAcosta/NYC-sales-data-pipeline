from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    if app.config['ENV'] == "production":
        app.config.from_object("config.ProductionConfig")
    elif app.config['ENV'] == "testing":
        app.config.from_object("config.TestingConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")

    db.init_app(app)
    api = Api(app)

    with app.app_context():
        from models import Transaction
        db.create_all()
        db.session.commit()

        from .resources import ZipcodeResources, NeighborhoodResources, DateResources
        api.add_resource(ZipcodeResources, '/zipcode/<int:zipcode>')
        api.add_resource(NeighborhoodResources, '/neighborhood/<neighborhood>')
        api.add_resource(DateResources, '/date')

    @app.route('/')
    def hello():
        return "Hello World"

    return app