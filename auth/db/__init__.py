from flask_sqlalchemy import SQLAlchemy

from auth.app import app

db: SQLAlchemy = SQLAlchemy(app)
