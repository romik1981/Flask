import click
from werkzeug.security import generate_password_hash

from blog.extensions import db


@click.command('init-db')
def init_db():
    from wsgi import app

    # import models for creating tables
    from blog.models import User

    db.create_all(app=app)


@click.command('create-init-user')
def create_init_user():
    from blog.models import User
    from wsgi import app
    email_in = input('email: ')
    password_in = input('password: ')

    with app.app_context():
        db.session.add(
            User(email=email_in, password=generate_password_hash(password_in))
        )
        db.session.commit()
