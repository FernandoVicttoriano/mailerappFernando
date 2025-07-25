from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Carga las variables desde el entorno (.env o Render Environment)
    db_user = os.getenv("FLASK_DATABASE_USER")
    db_password = os.getenv("FLASK_DATABASE_PASSWORD")
    db_host = os.getenv("FLASK_DATABASE_HOST")
    db_port = os.getenv("FLASK_DATABASE_PORT", "5432")
    db_name = os.getenv("FLASK_DATABASE")

    # Arma el string de conexión
    DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    # Configura la URI de la base de datos
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Configura la clave secreta y otros valores
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SENDGRID_API_KEY"] = os.getenv("SENDGRID_API_KEY")
    app.config["FROM_EMAIL"] = os.getenv("FROM_EMAIL")

    # Inicializa extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Registra blueprints si los tienes (ejemplo)
    # from .routes import main
    # app.register_blueprint(main)

    return app
