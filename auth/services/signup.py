from auth.dto.sign_up_request import SignUpRequest
from auth.db.models.User import User
from auth.db import db
from sqlalchemy.exc import IntegrityError
from enum import Enum


class Status(Enum):
    USERNAME_EXIST = 'USERNAME_EXIST'
    SUCCESS = 'SUCCESS'
    UNKNOWN_ERROR = 'UNKNOWN_ERROR'


def signup(request: SignUpRequest) -> str:
    try:
        user: User = User(request.username, request.password)
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        return Status.USERNAME_EXIST
    except Exception:
        return Status.UNKNOWN_ERROR

    return Status.SUCCESS
