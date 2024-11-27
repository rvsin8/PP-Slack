from flask import Blueprint, request, jsonify
import bcrypt  # Import bcrypt for password hashing
import jwt 
import datetime # To set an expiration time for the JWT
from backend.models import db, User # Import db and User froms moderls.py
import os

# Create a blueprint for authentication-relates routes --> A Blueprint in Flask helps modularize your application by grouping related routes together. 
# In this case, all authentication routes (like /register and /login) will belong to the auth blueprint.
auth_bp = Blueprint('auth', __name__)

SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_secret_key')

# User registration route
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    
    # Check if the username is already taken
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400
    
    # Hash the password before storing it
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user = User(username=username, password=hashed_password)

    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': f'User {username} registered successfully'}), 201


# User registration route
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    
    user = User.query.filter_by(username=username).first()

    if not user or not bcrypt.checkpw(password.encode('utf-8'), user.password):
        return jsonify({'error': 'Invalid username or password'}), 401

    # Generate JWT token with expiration time
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1) # Token expires in 1 hour
    token = jwt.encode({'user_id': user.id, 'exp' : expiration_time}, SECRET_KEY, algorithm='HS256')
    return jsonify({'message': 'Login successful', 'token': token}), 200 