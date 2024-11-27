from flask import Blueprint, request, jsonify
from models import db, Channel

channel_bp = Blueprint('channel', __name__)

# Create a new channel
@channel_bp.route('/create_channel', methods=['POST'])
def create_channel():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    # Validate input
    if not name:
        return jsonify({'error': 'Channel name is required'}), 400

    # Create the channel
    channel = Channel(name=name, description=description)
    db.session.add(channel)
    db.session.commit()

    return jsonify({'message': f'Channel {name} created successfully'}), 201
