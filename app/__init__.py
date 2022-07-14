import imp
from flask import Flask
from config import Config
<<<<<<< HEAD
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

=======

app = Flask(__name__)
app.config.from_object(Config)
>>>>>>> fce920aeff5892dd8c31e49866e910d7627fc61b

from app import routes, models