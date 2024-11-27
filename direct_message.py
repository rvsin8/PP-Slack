from flask import Blueprint, request, jsonify
from models import db, User, DirectMessage

direct_message_bp = Blueprint('direct_message', __name__)

@direct_message_bp.route('/direct_message', methods=['POST'])
def send_direct_message():
    data = request.get_json()
    sender_id = data.get('sender_id')
    receiver_id = data.get('receiver_id')
    content = data.get('content')

    # Validate Input
    if not content or not sender_id or not receiver_id:
        return jsonify({'error' : 'Sender ID, Receiver ID, and content are required'}), 400
    
    sender = User.query.get(sender_id)
    receiver = User.query.get(receiver_id)
    if not sender or not receiver:
        return jsonify({'error': 'Sender or Receiver not found'}), 404
    
    # Create and save the direct message
    direct_message = DirectMessage(sender_id=sender_id, receiver_id=receiver_id, content=content)
    db.session.add(direct_message)
    db.session.commit()

    return jsonify({'message' : 'Direct message sent successfully'}), 201

@direct_message_bp.route('/direct_message', methods=['GET'])
def get_direct_messages():
    sender_id = request.args.get('sender_id')
    receiver_id = request.args.get('receiver_id')
    
    # Fetch messages
    messages = DirectMessage.query.filter(
        (DirectMessage.sender_id == sender_id) & (DirectMessage.receiver_id == receiver_id) |
        (DirectMessage.sender_id == receiver_id) & (DirectMessage.receiver_id == sender_id)
    ).all()

    messages_list = [{'id': msg.id, 'content': msg.content, 'timestamp': msg.timestamp} for msg in messages]
    return jsonify({'messages': messages_list}), 200