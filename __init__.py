# project/__init__.py
from flask import Flask


def create_app():
    import models, routers
    app = Flask(__name__)
    app.config.from_pyfile("conf/config.py")
    models.init_app(app)
    routers.init_app(app)
    # services.init_app(app)
    return app
