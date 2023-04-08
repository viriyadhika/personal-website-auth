from flask import Blueprint, request, make_response
from auth.services.signup import signup as signupservice, Status
from auth.services.login import login as loginservice
from auth.dto.sign_up_request import SignUpRequest
from auth.dto.log_in_request import LogInRequest

signup_blueprint: Blueprint = Blueprint('signup', __name__)


@signup_blueprint.route('/signup')
def signup() -> str:
    result: Status = signupservice(SignUpRequest(request.get_json()))
    if (result == Status.SUCCESS):
        return make_response('Success', 200)
    if (result == Status.USERNAME_EXIST):
        return make_response('Username exist', 400)

    return make_response('Fail', 500)


@signup_blueprint.route('/login')
def login() -> str:
    result = loginservice(LogInRequest(request.get_json()))
    return result
