from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def create_app(config_name: str = 'development') -> Flask:
    # create and configure the app

    app = Flask(__name__)
        # Ensure it loads the configuration from the config.py file
    if config_name == 'testing':
        app.config.from_object('app.config.TestingConfig')
    elif config_name == 'development':
        app.config.from_object('app.config.DevelopmentConfig')
    elif config_name == 'production':
        app.config.from_object('app.config.ProductionConfig')
    else:
        raise ValueError("Invalid config name")

    # Enable CORS
    cors = CORS(app)

    # Initialize Plugins
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # configure swagger #
    SWAGGER_URL = "/api/docs"
    API_URL = "/static/swagger.json"
    SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL, API_URL, config={"app_name": "Recipe Tagger API"}
    )
    app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

    # Importing the Blueprints
    from app.routes import main as main_bp
    app.register_blueprint(main_bp)

    return app