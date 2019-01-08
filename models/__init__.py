# project/models/__init__.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    """
    db初始化
    """
    db.init_app(app)
