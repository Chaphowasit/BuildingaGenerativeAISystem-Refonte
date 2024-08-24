from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import random
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

# Path to placeholder images
PLACEHOLDER_IMAGES_PATH = os.path.join(app.static_folder, 'images')
PLACEHOLDER_IMAGES = os.listdir(PLACEHOLDER_IMAGES_PATH)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate-image', methods=['POST'])
def generate_image():
    # Simulate model inference by selecting a random placeholder image
    selected_image = random.choice(PLACEHOLDER_IMAGES) 
    return jsonify({'image_url': f'http://localhost:5000/static/images/{selected_image}'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
