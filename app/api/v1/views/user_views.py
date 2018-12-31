"""User view file."""

from flask import Blueprint, jsonify, make_response, request

from app.api.v1.models import user_models
from app.utilities.validator_functions import (check_number_format,
                                               check_name_format,
                                               check_username_format,
                                               check_password_strength,
                                               check_email_format,
                                               check_for_empty_string)


version1 = Blueprint('api-v1', __name__, url_prefix='/api/v1/auth')

user_views = user_models.UserModels()


@version1.route('/', methods=['GET'])
def index():
    """
    Root URL.
    Handles the welcoming message to the platform
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
    Method to create a user account.
    It handles the registration of a new user.
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
    except Exception as e:
        return jsonify({
            "Error": "Invalid {} Key field".format(e)
        }), 400

    if not check_name_format(first_name):
        return make_response(jsonify({
            "Error": "First name is invalid format"
        }), 400)

    if not check_name_format(last_name):
        return make_response(jsonify({
            "Error": "Last name is invalid format"
        }), 400)

    if not check_email_format(email):
        return make_response(jsonify({
            "Error": "Email is invalid format"
        }), 400)

    if not check_username_format(username):
        return make_response(jsonify({
            "Error": "Username is invalid format"
        }), 400)

    if check_for_empty_string(country):
        return make_response(jsonify({
            "Error": "Country cannot be empty"
        }), 400)

    if check_for_empty_string(confirm_password):
        return make_response(jsonify({
            "Error":
            "Confirm password cannot be empty, should be the same a password"
        }), 400)

    if not check_password_strength(password):
        return make_response(jsonify({
            "Error": "Password is not strong enough"
        }), 400)

    if not check_number_format(phone):
        return make_response(jsonify({
            "Error": "Phone number should be an integer"
        }), 400)

    user = user_views.get_by_email(email)
    if user:
        return make_response(jsonify({
            "Error":
            "User already exist with that email address, please login instead"
        }), 400)

    response = user_views.create_user(
        first_name, last_name, username, email, phone, country, password,
        confirm_password)

    return make_response(jsonify({
        "Message": "User created successfully",
        "details": response
    }), 201)


@version1.route('/login', methods=['POST'])
def login():
    """
    Method for logging in a registered user.
    """
    try:
        data = request.get_json()
        email = data["Email"]
        password = data["Password"]
    except Exception as e:
        error = e
        return jsonify({
            "Error": "Invalid {} Key field".format(error)
        }), 400

    user = user_views.get_by_email(email)
    if not user:
        return jsonify({
            "Error": "User has not yet been registered or user was deleted"
        }), 404

    if user:
        return jsonify({
            "Message": "User logged in successfully",
            "details": user
        }), 201


@version1.route('/users', methods=['GET'])
def fetch_all_users():
    """
    Method to retrieve all register users
    """
    user = user_views.get_all_users()
    if not user:
        return jsonify({
            "Error": "No user has been registered yet"
        }), 404
    if user:
        return jsonify({
            "Message": "Successfully found the following",
            "data": user
        }), 200


@version1.route('/users/<int:userid>', methods=['GET'])
def fetch_one_users(userid):
    """
    Method to retrieve only one register users by id
    """
    user = user_views.get_one_user(id=userid)
    if not user:
        return jsonify({
            "Error":
            "No user with user_id of {} has been registered yet".format(userid)
        }), 404
    if user:
        return jsonify({
            "Message": "Successfully found the following",
            "data": user
        }), 200


@version1.route('/delete/<int:userid>', methods=['DELETE'])
def delete_a_user(userid):
    """
    Method to delete a user from database
    """
    user = user_views.get_one_user(id=userid)
    if not user:
        return jsonify({
            "Error": "No user with that user_id of {} found".format(userid)
        }), 404

    user_models.user_data.remove(user)
    return jsonify({
        "Message": "Successfully delete user with user_id of {}".format(userid)
    }), 204
