from flask import Blueprint, request, jsonify
from server.models.user import User
from server.app import db
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return {"error": "Username and password required"}, 400

    if User.query.filter_by(username=username).first():
        return {"error": "Username already exists"}, 400

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.authenticate(password):
        token = create_access_token(identity=user.id)
        return {"access_token": token}, 200
    else:
        return {"error": "Invalid credentials"}, 401
