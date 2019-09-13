import os
from dotenv import load_dotenv
from os.path import join, dirname

# ---Method 1 for finding path
# project_folder = os.path.expanduser('~/flextime')

# ---Method 2 for finding path
project_folder = join(dirname(__file__))

load_dotenv(join(project_folder, '.env'))

class Config(object):
	SECRET_KEY = os.getenv("SECRET_KEY") # or "beb60f2682543ad4cd3a33d507f315aa"
	TEMPLATES_AUTO_RELOAD = True

	# take database URL from DATABASE_URL env var
	# if not defined, config a database named app.db in proj folder
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
								'sqlite:///' + join(project_folder, 'app.db')
	# to disable a signaling feature
	SQLALCHEMY_TRACK_MODIFICATIONS = False