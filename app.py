
from flask import Flask
from routes.mainroutes import osmiumRoutes

from flask_login import LoginManager
# import os


# import logging
# logging.basicConfig(level=logging.DEBUG)

osmium = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(osmium)

osmium.register_blueprint(osmiumRoutes)


osmium.run(debug=True,port=5000)
