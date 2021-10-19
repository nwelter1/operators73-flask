from flask import Flask
from config import Config
from .site.routes import site
from .authentication.routes import auth
from flask_migrate import Migrate
from .models import db


#instantiating a new flask app
app = Flask(__name__)
app.config.from_object(Config)

# Registering Blueprints to use within the scope of our whole app
app.register_blueprint(site)
app.register_blueprint(auth)

# instantiating db within the scope of our app
db.init_app(app)

# giving Flask migrate access to app and DB models
migrate = Migrate(app, db)

