from flask import Flask
from backend.auth import auth_bp  # Import the blueprint from auth.py
from flask_sqlalchemy import SQLAlchemy
from backend.message import message_bp  # Import the message blueprint from message.py
from backend.models import db  # Import db from models.py
from backend.channel import channel_bp  # Import the channel blueprint from channel.py
from backend.direct_message import direct_message_bp  # Import the direct message blueprint
from flask_migrate import Migrate
from auth import auth_bp  # Import the blueprint from auth.py


app = Flask(__name__)

# Configure PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rav:new_password@localhost/slack_clone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Initialize SQLAlchemy
db.init_app(app)  # Linking db object to the app

# Register the auth blueprint
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(message_bp, url_prefix='/message')
app.register_blueprint(channel_bp, url_prefix='/channel')  # Register the channel blueprint
app.register_blueprint(direct_message_bp, url_prefix='/direct_message')


@app.route('/')  # Decorator that maps the root URL to the home function
def home():
    return 'Welcome to Slack Clone!'

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=3000)
