from flask import Blueprint, request, jsonify # Core framework to define routes and handle HTTP requests
from backend.models import db, User, Channel, Message  # Import db from models.py
from flask import current_app as app

message_bp = Blueprint('message', __name__)

@message_bp.route('/channel/<int:channel_id>/message', methods=['POST'])
def send_message(channel_id):
    data = request.get_json()
    content = data.get('content')
    user_id = data.get('user_id')

    # Validate input
    if not content or not user_id:
        return jsonify({'error': 'Message content and user ID are required'}), 400
    
    # Check if the user exists
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
     # Check if the channel exists
    channel = Channel.query.get(channel_id)
    if not channel:
        return jsonify({'error': 'Channel not found'}), 404
    
    # Create and save the new message
    message = Message(user_id=user_id, channel_id=channel_id, content=content)
    db.session.add(message)
    db.session.commit()
    
    return jsonify({'message': 'Message sent successfully'}), 201

@message_bp.route('/channel/<int:channel_id>/message', methods=['GET'])
def get_message(channel_id):
    channel = Channel.query.get(channel_id)
    if not channel:
        return jsonify({'error': 'Channel not found'}), 404
    
    # Create and save the new message
    messages = Message.query.filter_by(channel_id=channel_id).all()
    messages_list = [
        { 
            'id': message.id, 
            'content': message.content, 
            'timestamp': message.timestamp, 
            'user': message.user.username 
        } for message in messages

    ]
    
    return jsonify({'messages': messages_list}), 200

