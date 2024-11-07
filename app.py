from flask import Flask
from routes.plants import plants_bp

# Initializing Flask application
app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(plants_bp)

# Adding a route for the root URL
@app.route('/')
def home():
    return "Welcome to the Herbiscus API!"

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)