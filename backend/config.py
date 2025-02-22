from decouple import config

# Configuration class. Get the values from the ../.env file
class Config:
    FLASK_ENV = config("FLASK_ENV")
    SECRET_KEY = config("SECRET_KEY")
    DB_HOST = config("DB_HOST")
    DB_PORT = config("DB_PORT")
    DB_NAME = config("DB_NAME")
    DB_USER = config("DB_USER")
    DB_PASSWORD = config("DB_PASSWORD")
    
    # Database URI #postgresql://user:password@host:port/database
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
