from blog.app import create_app

app = create_app()





# from blog.app import create_app, db
# from flask import redirect
# from blog.models import User

# app = create_app()


# @app.route("/")
# def index():
#     return redirect('/users/')


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        debug=True,
        port=5000
    )




# from blog.app import app
# if __name__ == "__main__":
#     app.run(
#         host="0.0.0.0",
#         debug=True,
#     )
