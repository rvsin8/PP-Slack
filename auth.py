from flask import Blueprint, request, jsonify
import bcrypt  # Import bcrypt for password hashing
import uuid # For generating a simple session token

# Create a blueprint for authentication-relates routes --> A Blueprint in Flask helps modularize your application by grouping related routes together. 
# In this case, all authentication routes (like /register and /login) will belong to the auth blueprint.
auth_bp = Blueprint('auth', __name__)

# In-memory user store (to be replaced with database later)
users = {}

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
    if username in users:
        return jsonify({'error': 'Username already exists'}), 400
    
    # Hash the password before storing it
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    # Store user in the in-memory dictionary
    users[username] = hashed_password
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
    
    # Check if the username is already taken
    if username not in users:
        return jsonify({'error': 'Invalid username or password'}), 400

    # Verify the password
    stored_password = users[username]

    if not bcrypt.checkpw(password.encode('utf-8'), stored_password):
        return jsonify({'error': 'Invalid username or password'}), 401

    # Generate simple session token
    token = str(uuid.uuid4()) 
    return jsonify({'message': 'Login successful', 'token': token}), 200 