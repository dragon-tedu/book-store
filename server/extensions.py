from flask_redis import Redis

from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine
from server.models import User
from pymongo import MongoClient

db = MongoEngine()
jwt = JWTManager()
redis = Redis()


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User().get_by_id(user_id=identity['_id'])


@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    token_in_redis = redis.get(jti)
    return token_in_redis is not None
