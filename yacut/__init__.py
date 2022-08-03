from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import Config

SHORT_LINK_LEN = 6
SHORT_LINK_TEMPLATE = r'^[a-zA-Z0-9]{,16}$'

app = Flask(
    __name__,
    static_folder='../html',
    template_folder='../html/templates',

)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import api_views, error_handlers, views
