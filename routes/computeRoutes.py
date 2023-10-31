from flask import Blueprint, jsonify, request
from models.db import get_db
from models.user import User
from models.db import SessionLocal


api_routes = Blueprint('api_data', __name__)


@api_routes.route('/api/data')
def compute_route():
    # db = get_db()
    # Replace this with your data retrieval logic
    data = {"message": "API data here11"}
    new_user = User(username='shubhammandlas',
                    email="shubham.mandlas@gmail.com")
    print('New User-- ', new_user)
    # db.add(new_user)
    with SessionLocal() as db:
        # db.add(new_user)
        # db.commit()
        user_data = {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email
        }
        return jsonify(user_data)

    # return jsonify(data)
