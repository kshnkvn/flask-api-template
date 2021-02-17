from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    '''Creating a Flask application.'''

    app = Flask(__name__, instance_relative_config=False)

    if app.config['ENV'] == 'production':
        app.config.from_object('config.Config')
    else:
        app.config.from_object('config.DevConfig')

    db.init_app(app)

    with app.app_context():
        from app.routes import main

        app.register_blueprint(main)

        db.create_all()

        return app
