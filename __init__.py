import os
from flask import Flask
from jinja2 import FileSystemLoader, ChoiceLoader
from pymongo import MongoClient
from config import Config


mongo = MongoClient('mongodb://localhost:27017/')
db = mongo['wego']


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Create loaders for the two template folders
    # Construct paths to the two template folders using the os module
    templates_folder1 = os.path.join(os.path.dirname(__file__), '../supply_fe')
    templates_folder2 = os.path.join(os.path.dirname(__file__), '../common_services_fe')

    loader1 = FileSystemLoader(templates_folder1)
    loader2 = FileSystemLoader(templates_folder2)


    # Create a choice loader that will choose between the two loaders
    # based on the name of the template being loaded
    choice_loader = ChoiceLoader([loader1, loader2])

    # Set the Flask app's jinja_loader attribute to the choice loader
    app.jinja_loader = choice_loader

    # Register blueprints for the various parts of the app
    from .views import views
    from .auth import auth
    from supply_order_handler_api.order_rest_api import order_rest_api  

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(order_rest_api, url_prefix='/')

    return app
