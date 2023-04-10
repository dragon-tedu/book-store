
from flask import Blueprint, jsonify, request
from datetime import timedelta

from server.validate import validate_email_and_password, validate_user
from server.models import User
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token,get_jwt
from server.extensions import redis

userRouter = Blueprint('users', __name__)

@userRouter.route("/", methods=['POST'])
def add_user():
    try:
        user = request.get_json()
        if not user:
            return {
                "message": "Please provide user details",
                "data": None,
                "error": "Bad request"
            }, 400
        is_validated = validate_user(**user)
        if is_validated is not True:
            return dict(message='Invalid data', data=None,
                        error=is_validated), 400
        user = User().create(**user)
        if not user:
            return {
                "message": "User already exists",
                "error": "Conflict",
                "data": None
            }, 409
        return {
            "message": "Successfully created new user",
            "data": user
        }, 201
    except Exception as e:
        return {
            "message": "Something went wrong",
            "error": str(e),
            "data": None
        }, 500


@userRouter.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        if not data:
            return {
                "message": "Please provide user details",
                "data": None,
                "error": "Bad request"
            }, 400
        # validate input
        is_validated = validate_email_and_password(
            data.get('email'), data.get('password'))
        if is_validated is not True:
            return dict(message='Invalid data', data=None, error=is_validated), 400
        user = User().login(
            data["email"],
            data["password"]
        )
        if user:
            try:
                # token should expire after 24 hrs
                user["token"] = create_access_token(identity={
                    "_id": user['_id']
                    })
                return {
                    "message": "Successfully fetched auth token",
                    "data": user
                }
            except Exception as e:
                return {
                    "error": "Something went wrong",
                    "message": str(e)
                }, 500
        return {
            "message": "Error fetching auth token!, invalid email or password",
            "data": None,
            "error": "Unauthorized"
        }, 404
    except Exception as e:
        return {
            "message": "Something went wrong!",
            "error": str(e),
            "data": None
        }, 500


@userRouter.route("/logout", methods=["DELETE"])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    redis.set(jti, "", ex=timedelta(hours=1))
    return jsonify(msg="Access token revoked")

@userRouter.route('/', methods=['GET'])
@jwt_required()
def protected():
    # We can now access our sqlalchemy User object via `current_user`.
    current_user_id = get_jwt_identity()
    # return jsonify(
    #     _id=current_user._id,
    #     name=current_user.name,
    #     email=current_user.email,
    # )
    return jsonify(
        _id=current_user_id['_id']
    )


@userRouter.route("/", methods=['PUT'])
@jwt_required()
def update_current_user():
    try:
        current_user = get_jwt_identity()
        user = request.get_json()
        if user['name']:
            user = User().update(current_user["_id"], user["name"])
            return jsonify({
                "message": "successfully updated account",
                "data": user
            }), 201
    except Exception as e:
        return jsonify({
            "message": "Failed to update account",
            "error": str(e),
            "data": None
        }), 401


@userRouter.route("/", methods=["DELETE"])
@jwt_required()
def disable_user():
    try:
        current_user = get_jwt_identity()
        User().disable_account(current_user["_id"])
        return jsonify({
            "message": "successfully disabled acount",
            "data": None
        }), 204
    except Exception as e:
        return jsonify({
            "message": "failed to disable account",
            "error": str(e),
            "data": None
        }), 400
