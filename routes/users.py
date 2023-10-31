from flask import Blueprint

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/addUser')
def user_route():
    return "User Route"
