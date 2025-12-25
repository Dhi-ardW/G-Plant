from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'AMRH'
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(app.instance_path, DB_NAME)
    
    os.makedirs(app.instance_path, exist_ok=True)
    db.init_app(app)

    from .models import User

    # login Logic
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id) :
        return User.query.get(int(id))

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    return app

def create_database(app) :
   db_path = os.path.join(app.instance_path, DB_NAME)
   if not path.exists(db_path):
        db.create_all(app=app)
        print('database has created')
