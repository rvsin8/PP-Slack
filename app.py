from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to Slack Clone!'

if __name__ == "__main__":  # Corrected "__main__" with double underscores
    app.run(debug=True, host='0.0.0.0', port=3000)