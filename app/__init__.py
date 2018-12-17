"""Initialize app."""
import os
from flask import Flask
from app.api.v1.views.user_views import version1
from dotenv import load_dotenv

from config import app_config


def create_app(config_name):
    """Create the app with the desired environment."""
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])
    app.register_blueprint(version1)

    return app


# Used for loading the dotenv
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

tw_consumer_key = os.getenv('FLASK_ENV')
