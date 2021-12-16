from flask import Flask
from flask_login import LoginManager


osmium = Flask(__name__)

# import os


# import logging
# logging.basicConfig(level=logging.DEBUG)

login_manager = LoginManager()
login_manager.init_app(osmium)


from flaskmium.modules import pageroute
from flaskmium.modules import requestroute
from flaskmium.modules import failroute

