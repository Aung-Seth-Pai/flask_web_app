# main app, configurations, extension frameworks, database

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# __name__ >> name of module in which it is used >> "__init__.py"
# flask use the directory of module to locate templates, statics, etc
app = Flask(__name__)
app.config.from_object(Config)

# initialize flask extensions
db = SQLAlchemy(app)		# database
migrate = Migrate(app, db)	# database migration engine

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# models module >> to define db structure
# route is always imported at the bottom
from app import routes, models

