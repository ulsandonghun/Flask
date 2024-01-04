from flask import Blueprint, jsonify
from app.models.user import User

api_routes = Blueprint('api', __name__)

@api_routes.route('/users', methods=['GET'])
def get_users():
    users = User.query_all()
    user_list = [{'id': user.id, 'username': user.username} for user in users]
    return jsonify({'users': user_list})
