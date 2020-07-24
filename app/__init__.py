from flask import Flask
from app.schema import Schema
from app.model import Mongo


def create_app(*config_cls):
    app = Flask(__name__)

    for config in config_cls:
        app.config.from_object(config)

    print(
        "[INFO] Flask application initialized with {0}".format(
            [config.__name__ for config in config_cls]
        )
    )

    Mongo(app)
    Schema(app)

    return app
