import click
from werkzeug.security import generate_password_hash

from blog.extensions import db
from wsgi import app


@click.command('init-db')
def init_db():
    from wsgi import app

    # import models for creating tables
    from blog.models import User

    db.create_all(app=app)
    
    print("done!")

@click.command('create-init-user')
def create_init_user():
    from blog.models import User
    from wsgi import app
    
    #name_in = input('name: ')
    email_in = input('email: ')
    password_in = input('password: ')
    
    with app.app_context():
        db.session.add(
            User(email=email_in, password=generate_password_hash(password_in))
        )
        db.session.commit()

    #print("done! created users: ", name_in)


@click.command('create-superusers')
def create_superuser():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models import User
    
    admin = User(username="admin", is_staff=True)
    db.session.add(admin)
    db.session.commit()
    print("done! created users:", admin)
