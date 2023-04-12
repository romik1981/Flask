from flask_login import UserMixin

from blog.app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    is_staff = db.Column(db.Boolean, default=False)

    def __init__(self, email, password, name, is_staff):
        self.email = email
        self.password = password
        self.name = name
        self.is_staff = is_staff

# flask db migrate -m "add is_staff and name field to user model"
# flask db upgrade