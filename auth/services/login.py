from auth.dto.log_in_request import LogInRequest
from auth.db.models.User import User


def login(request: LogInRequest):
    queried_user: User = User.query.filter_by(
        username=request.username).first()
    if (queried_user != None and request.password == queried_user.password):
        return 'Success'
    return 'Failed'
