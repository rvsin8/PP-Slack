from flask import Flask #Core framework to define routes and handle HTTP requests

app = Flask(__name__) #Creates instance of Flask class, __name__ tells Flask the location of the current python module.

@app.route('/') #Decorator that maps the root url to the home function
def home():
    return 'Welcome to Slack Clone!'

if __name__ == "__main__":  # Corrected "__main__" with double underscores, checks if the scrupt it being run directly.
    app.run(debug=True, host='0.0.0.0', port=3000)