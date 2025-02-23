from decouple import config

# Configuration class. Get the values from the ../.env file
class Config:
    FLASK_ENV: str = config("FLASK_ENV")
    SECRET_KEY: str = config("SECRET_KEY")
    DB_HOST: str = config("DB_HOST")
    DB_PORT: str = config("DB_PORT")
    DB_NAME: str = config("DB_NAME")
    DB_USER: str = config("DB_USER")
    DB_PASSWORD: str = config("DB_PASSWORD")
    
    # Database URI #postgresql://user:password@host:port/database
    SQLALCHEMY_DATABASE_URI: str = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False