import os
from datetime import timedelta
from dotenv import load_dotenv
load_dotenv()


class BaseConfig(object):
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "RS256")
    JWT_PRIVATE_KEY = open('rs256.pem').read()
    JWT_PUBLIC_KEY = open('rs256.pub').read()
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    MONGODB_SETTINGS = {
        "db": os.getenv("MONGO_DATABASE", "stt-queue"),
        "host": os.getenv(
            "MONGO_URI",
            "mongodb://localhost:27017/?retryWrites=true&serverSelectionTimeoutMS=5000&connectTimeoutMS=10000",
        ),
    }
    SERVICE_NAME = os.getenv("SERVICE_NAME", "store-book")

    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = os.getenv("REDIS_PORT", 6379)
    REDIS_DB = os.getenv("REDIS_DB", 0)


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG = (True,)
    BCRYPT_LOG_ROUNDS = (4,)


class ProductionConfig(BaseConfig):
    """Production configuration."""

    DEBUG = False


class TestingConfig(BaseConfig):
    """Testing configuration."""

    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    BCRYPT_LOG_ROUNDS = 4


app_config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}
