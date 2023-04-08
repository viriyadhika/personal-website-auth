from auth.app import app
from auth.db import db
from auth.db.models.User import User
from auth.routes.signup import signup_blueprint
from flask import Flask

app.register_blueprint(signup_blueprint)


def create_app() -> Flask:
    return app
