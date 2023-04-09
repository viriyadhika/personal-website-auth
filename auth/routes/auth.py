from flask import Blueprint, request, make_response
from auth.services.signup import signup as signupservice, Status
from auth.services.login import login as loginservice
from auth.dto.sign_up_request import SignUpRequest
from auth.dto.log_in_request import LogInRequest

auth_blueprint: Blueprint = Blueprint('signup', __name__)


@auth_blueprint.route('/signup')
def signup() -> str:
    return signupservice(SignUpRequest(request.get_json()))


@auth_blueprint.route('/login')
def login() -> str:
    return loginservice(LogInRequest(request.get_json()))
