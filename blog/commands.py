
import click
from werkzeug.security import generate_password_hash

from blog.extensions import db


# @click.command('init-db')
# def init_db():
#     from wsgi import app

#     # import models for creating tables
#     from blog.models import User

#     db.create_all(app=app)

#     print('done!')



@click.command('create-init-user')
def create_init_user():
    
    from blog.models import User
    from wsgi import app
    

    first_name_in = input('first_name: ')
    last_name_in = input('last_name: ')
    email_in = input('email: ')
    password_in = input('password: ')
    # is_staff_in = input('is_staff: ')
    
    # if is_staff_in == '1':
    #     is_staf_in = True
    # else: is_staff_in = False

    with app.app_context():
        db.session.add(
            User(first_name=first_name_in, last_name=last_name_in, email=email_in, password=generate_password_hash(password_in))
        )
        db.session.commit()
    
    print('create user: ', first_name_in, last_name_in)


@click.command('create-init-tags')
def create_init_tags():
    from blog.models import Tag
    from wsgi import app

    with app.app_context():
        tags = ('flask', 'django', 'python', 'gb', 'sqlite')
        for item in tags:
            db.session.add(Tag(name=item))
        db.session.commit()
    click.echo(f'Created tags: {", ".join(tags)}')
 