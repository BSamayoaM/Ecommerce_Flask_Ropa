from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from forms import RegistrationForm,LoginForm

db = SQLAlchemy()
DB_NAME = "database.db"


def crear_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "123456"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    from productos.routes import productos
    from compras.routes import compras
    from usuarios.routes import usuarios
    from ventas.routes import ventas
    app.register_blueprint(productos)
    app.register_blueprint(compras)
    app.register_blueprint(usuarios)
    app.register_blueprint(ventas)

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
