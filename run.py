from app import create_app
from app.config.dev import DevConfig

if __name__ == "__main__":
    app = create_app(DevConfig)

    app.run(**DevConfig.RUN_SETTING)
