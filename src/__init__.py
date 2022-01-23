from flask import Flask

def create_app():
    app = Flask(__name__)

    from src.after_login.after_login_routes import views
    from src.after_login.lectures import lectures

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(lectures, url_prefix='/')

    return app
