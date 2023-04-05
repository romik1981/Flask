# from flask import Blueprint, render_template
# from flask_login import login_required
# from werkzeug.exceptions import NotFound

# from blog.models import User

# user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


# @user.route('/')
# def user_list():
#     users = User.query.all()
#     return render_template(
#         'users/list.html',
#         users=users,
#     )


# @user.route('/<int:pk>')
# @login_required
# def profile(pk: int):
#     selected_user = User.query.filter_by(id=pk).one_or_none()
#     if not selected_user:
#         raise NotFound(f"User #{pk} doesn't exist!")

#     return render_template(
#         'users/profile.html',
#         user=selected_user,
#     )







from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

user = Blueprint("user", __name__, url_prefix="/users", static_folder="../static")
USERS = {
    1: {"name": "Ivan"},
    2: {"name": "Jon"},
    3: {"name": "Mary"}
}


@user.route("/")
def user_list():
    return render_template(
        "users/list.html",
        users=USERS
    )


@user.route("/<int:pk>")
def get_user(pk: int):
    if pk in USERS:
        user_raw = USERS[pk]
    else:
        raise NotFound("User id:{}, not found".format(pk))
    return render_template(
        "users/details.html",
        user_name=user_raw["name"]
    )


def get_user_name(pk: int):
    if pk in USERS:
        user_name = USERS[pk]["name"]
    else:
        raise NotFound("User id:{}, not found".format(pk))
    return user_name
