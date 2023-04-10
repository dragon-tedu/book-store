from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token,get_jwt

from server.validate import validate_book
from server.models import Books


bookRouter = Blueprint('books', __name__)

@bookRouter.route("/",methods =['POST'])
@jwt_required
def add_book(current_user):
    try:
        book = dict(request.form)
        if not book:
            return {
                "message": "Invalidate data, you need to give the book title,cover image, author id",
                "data": None,
                "error":"Bad request"
            },400
        if not request.files['cover_image']:
            return {
                "message": "cover image is required",
                "data": None
            }, 400
        book["image_url"] = request.host_url+"static/books/"+save_pic(request.files["cover_image"])
        is_validated = validate_book(**book)
        if is_validated is not True:
            return {
                "message": "Invalidate data,you need to give the book title, cover image, author id.",
                "data": None,
                "error":"Bad Request"
            },400
        book = Books().create(**book)
        if not book:
            return {
                "message": "The book have been created by user",
                "data": None,
                "error": "Bad request"
            },400
        return  jsonify({
            "message": "The book has been  created by user",
            "data": book
        }),201
    except Exception as e:
        return jsonify({
            "message": "failed to create new book",
            "error": str(e),
            "data": None
        }), 500
    # end try