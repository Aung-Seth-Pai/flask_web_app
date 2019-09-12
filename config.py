import os
from dotenv import load_dotenv

project_folder = os.path.expanduser('~/flextime')
load_dotenv(os.path.join(project_folder, '.env'))

class Config(object):
	SECRET_KEY = os.getenv("SECRET_KEY")
	TEMPLATES_AUTO_RELOAD = True

# or "beb60f2682543ad4cd3a33d507f315aa"
