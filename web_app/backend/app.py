from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import random
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
CORS(app)  # Enable CORS

# Path to placeholder images
PLACEHOLDER_IMAGES_PATH = os.path.join(app.static_folder, 'images')
PLACEHOLDER_IMAGES = os.listdir(PLACEHOLDER_IMAGES_PATH)

PLACEHOLDER_VIDEOS_PATH = os.path.join(app.static_folder, 'videos')
PLACEHOLDER_VIDEOS = os.listdir(PLACEHOLDER_VIDEOS_PATH)

# Base URL for serving images
BASE_URL = os.getenv('BASE_URL', 'http://localhost:5000')  # Default to localhost for development

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate-image', methods=['POST'])
def generate_image():
    # Simulate model inference by selecting a random placeholder image
    # receive prompt from frontend and create image based on prompt then return the image
    selected_image = random.choice(PLACEHOLDER_IMAGES)
    return jsonify({'image_url': f'{BASE_URL}/static/images/{selected_image}'})

@app.route("/generate-video", methods=['POST'])
def generate_video():
    # Simulate model inference by selecting a random placeholder image
    # receive prompt from frontend and create video based on prompt then return the video
    selected_video = random.choice(PLACEHOLDER_VIDEOS)
    return jsonify({'video_url': f'{BASE_URL}/static/videos/{selected_video}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
