
from flask import Flask
from routes.mainroutes import osmiumRoutes
# import os


# import logging
# logging.basicConfig(level=logging.DEBUG)

osmium = Flask(__name__)

osmium.register_blueprint(osmiumRoutes)


osmium.run(debug=True,)
