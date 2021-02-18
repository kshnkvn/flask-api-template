from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_obj=None):
    '''Creating a Flask application.
    
    Parameters:
        config_obj: object
            Class object with properties as Flask settings
    '''

    app = Flask(__name__, instance_relative_config=False)

    if config_obj:
        app.config.from_object(config_obj)
    elif app.config['ENV'] == 'production':
        app.config.from_object('config.Config')
    else:
        app.config.from_object('config.DevConfig')

    db.init_app(app)

    with app.app_context():
        from app.routes import main

        app.register_blueprint(main)

        db.create_all()

        return app
