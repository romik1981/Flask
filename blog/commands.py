import click
from werkzeug.security import generate_password_hash

from blog.extensions import db


@click.command('init-db')
def init_db():
    from wsgi import app

    # import models for creating tables
    from blog.models import User

    db.create_all(app=app)

    print('done!')


@click.command('create-init-user')
def create_init_user():
    
    from blog.models import User
    from wsgi import app
    
    email_in = input('email: ')
    password_in = input('password: ')

    name_in = input('name: ')
    email_in = input('email: ')
    password_in = input('password: ')
    is_staff_in = input('is_staff: ')

    if is_staff_in == '1':
        is_staff_in = True
    else: is_staff_in = False

    with app.app_context():
        db.session.add(
            User(name=name_in, email=email_in, password=generate_password_hash(password_in), is_staff=is_staff_in)
        )
        db.session.commit()
    
    print('create user: ', name_in)
