from auth.dto.sign_up_request import SignUpRequest
from auth.db.models.User import User
from auth.db import db
from sqlalchemy.exc import IntegrityError
from enum import Enum
from auth.utils.password_hash import generate_salt, hash_password
from auth.utils.error_message import create_error_message
from flask import abort, make_response


class Status(Enum):
    USERNAME_EXIST = 'USERNAME_EXIST'
    SUCCESS = 'SUCCESS'
    UNKNOWN_ERROR = 'UNKNOWN_ERROR'


def signup(request: SignUpRequest) -> str:
    try:
        salt = generate_salt()
        user: User = User(request.username, hash_password(
            request.password, salt), salt, 'USER')
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        return abort(make_response(create_error_message('Username already exist'), 400))
    except Exception:
        return abort(make_response(create_error_message('Something went wrong'), 500))

    return {'response': 'Success'}
