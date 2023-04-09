from auth.dto.log_in_request import LogInRequest
from auth.db.models.User import User
from auth.utils.password_hash import hash_password
from auth.utils.error_message import create_error_message
from flask import abort, make_response
from flask_jwt_extended import create_access_token


def login(request: LogInRequest):
    try:
        queried_user: User = User.query.filter_by(
            username=request.username).first()
    except:
        abort(make_response(create_error_message('Something went wrong'), 500))

    if (queried_user == None or hash_password(request.password, queried_user.salt) != queried_user.password):
        abort(make_response(create_error_message(
            'Username or password is wrong'), 401))

    return {'access_token': create_access_token(identity=request.username)}
