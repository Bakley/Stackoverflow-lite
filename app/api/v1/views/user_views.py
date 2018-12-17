from flask import Blueprint, jsonify, json, make_response, request

from app.api.v1.models import user_models
from app.utilities.validator_functions import check_number_format, check_name_format, check_username_format, check_password_strength, check_email_format


version1 = Blueprint('api-v1', __name__, url_prefix='/api/v1/auth')

user_views = user_models.UserModels()


@version1.route('/', methods=['GET'])
def index():
    """
    Root URL
    """
    welcome_message = "Hey! Welcome to Stackoverflow Lite"

    response = jsonify({
        "Status": "Success",
        "Message": welcome_message
    }), 200

    return response


@version1.route('/signup', methods=['POST'])
def register():
    """
    Method to create a user account
    """
    try:
        data = request.get_json()
        first_name = data["First Name"]
        last_name = data["Last Name"]
        username = data["Username"]
        email = data["Email"]
        phone = data["Phone Number"]
        country = data["Country"]
        password = data["Password"]
        confirm_password = data["Confirm Password"]
    except Exception:
        return make_response(jsonify({
            "Message": "Invalid key field"
        }), 400)

    if not check_name_format(first_name):
        return make_response(jsonify({
            "Message": "First name is invalid format"
        }), 400)

    if not check_name_format(last_name):
        return make_response(jsonify({
            "Message": "Last name is invalid format"
        }), 400)

    if not check_email_format(email):
        return make_response(jsonify({
            "Message": "Email is invalid format"
        }), 400)

    if not check_username_format(username):
        return make_response(jsonify({
            "Message": "Username is invalid format"
        }), 400)

    if not check_password_strength(password):
        return make_response(jsonify({
            "Message": "Password is not strong enough"
        }), 400)

    if not check_number_format(phone):
        return make_response(jsonify({
            "Message": "Phone number should be an integer"
        }), 400)

    response = user_views.create_user(
        first_name, last_name, username, email, phone, country, password, confirm_password)

    return make_response(jsonify({
        "Message": "User created successfully",
        "data": response
    }), 201)


@version1.route('/login', methods=['POST'])
def login():
    """
    Method for logging in a signed up user.
    """

    data = request.get_json()
    email = data["Email"]
    password = data["Password"]

    user = user_views.get_by_email(email)
    if not user:
        return jsonify({
            "Message": "User has not yet been registered."
        }), 404

    if user:
        return jsonify({
            "Message": "User logged in successfully",
            "data": user
        }), 200


@version1.route('/users', methods=['GET'])
def fetch_all_users():
    """
    Method to retrieve all register users
    """
    user = user_views.get_all_users()
    if not user:
        return jsonify({
            "Message": "No user has been registered yet"
        })
    if user:
        return jsonify({
            "Message": "Successfully found the following",
            "data": user
        })


@version1.route('/delete/<int:id>', methods=['DELETE'])
def delete_a_user(id):
    """
    Method to delete a user from database
    """
    user = user_views.get_one_user(id)
    if not user:
        return jsonify({
            "Message": "No user with that Id found"
        })
    user_models.user_data.remove(user)
    return jsonify({
        "Message": "Successfully delete user"
    })
