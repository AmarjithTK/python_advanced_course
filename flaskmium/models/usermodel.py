
from flask_login import UserMixin
from flaskmium import login_manager


usercred = {'amar@gmail.com':{"password":'123456'}}

import flask_login

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(user):

    loggedUser = User()
    loggedUser.id = user

    return loggedUser
    