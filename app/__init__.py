from flask import Flask

# Define the WSGI application object
application = Flask(__name__)

# Configurations
application.config.from_object('config')
