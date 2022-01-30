from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"


def crear_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "123456"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    from .views import views
    from .auth import auth
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    from models import Usuarios,Productos
    crear_bd(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Usuarios.query.get(int(id))

    return app


def crear_bd(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Base de datos creada')
