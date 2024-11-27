from flask import Blueprint, request, jsonify
from models import db, Channel, User, ChannelUser
  
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
    
    # Check if the channel already exists
    existing_channel = Channel.query.filter_by(name=name).first()
    if existing_channel:
        return jsonify({'error': f'Channel with name {name} already exists'}), 400

    # Create the channel
    channel = Channel(name=name, description=description)
    db.session.add(channel)
    db.session.commit()

    return jsonify({'message': f'Channel {name} created successfully'}), 201

# Add User to Channel
@channel_bp.route('/channel/<int:channel_id>/add_user', methods=['POST'])
def add_user_to_channel(channel_id):
    data = request.get_json()
    user_id = data.get('user_id')

    channel = Channel.query.get(channel_id)
    if not channel:
        return jsonify({'error': 'Channel not found'}), 404
    
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    if channel.is_private:
        return jsonify({'error': 'This is a private channel, cannot add user directly'}), 403
    
    channel_user = ChannelUser(user_id=user_id, channel_id=channel_id)
    db.session.add(channel_user)
    db.session.commit()

    return jsonify({'message': f'User {user.username} added to channel {channel.name}'}), 200

# Search Channels
@channel_bp.route('/search', methods=['GET'])
def search_channels():
    query = request.args.get('query', '')
    channels = Channel.query.filter(
        Channel.name.like(f'%{query}%') | Channel.description.like(f'%{query}%')
    ).all()

    channels_list = [{'id': channel.id, 'name': channel.name, 'description': channel.description} for channel in channels]

    return jsonify({'channels': channels_list}), 200

# Users can join Public Channels
@channel_bp.route('/channel/<int:channel_id>/join', methods=['POST'])
def join_channel(channel_id):
    user_id = request.get_json().get('user_id')

    channel = Channel.query.get(channel_id)
    if not channel:
        return jsonify({'error': 'Channel not found'}), 404

    # Check if the channel is private
    if channel.is_private:
        return jsonify({'error': 'This is a private channel, cannot join directly.'}), 403

    # Add user to the channel
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    channel_user = ChannelUser(user_id=user_id, channel_id=channel_id)
    db.session.add(channel_user)
    db.session.commit()

    return jsonify({'message': f'User {user.username} joined channel {channel.name}'}), 200


@channel_bp.route('/channel/<int:channel_id>', methods=['GET'])
def get_channel(channel_id):
    channel = Channel.query.get(channel_id)
    if not channel:
        return jsonify({'error': 'Channel not found'}), 404
    
    channel_data = {
        'id': channel.id,
        'name': channel.name,
        'description': channel.description,
    }
    
    return jsonify({'channel': channel_data}), 200