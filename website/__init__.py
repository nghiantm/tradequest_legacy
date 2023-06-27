from flask import Flask
from .views import views
from .routes import routes

def create_app():
    app = Flask(__name__, template_folder="./templates",
                static_folder="./assets")
    app.config['SECRET KEY'] = 'dhawdiojad'

    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(routes, url_prefix='/')

    return app

