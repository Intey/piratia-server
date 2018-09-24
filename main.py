from flask import Flask
from server.routes.main import bp

app = Flask(__name__)

app.register_blueprint(bp)
