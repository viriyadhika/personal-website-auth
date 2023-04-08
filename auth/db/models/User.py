from auth.db import db
from sqlalchemy import Column, Integer, String


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    password = Column(String(64))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self) -> str:
        return f'<User {self.username}>'
