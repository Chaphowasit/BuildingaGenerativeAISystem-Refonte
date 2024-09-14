import os
import sys

import torch
from diffusers import (
    DiffusionPipeline,
    DPMSolverMultistepScheduler,
    StableDiffusionPipeline,
)
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

from text_to_video.video_gen import text_to_video_model
from text_to_image.image_gen import text_to_image_model

# load environment variables, authorization token, and device
load_dotenv()
authorization_token = os.getenv("AUTH_TOKEN", "")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the text-to-image model
stable_diff_model = "CompVis/stable-diffusion-v1-4"
stable_diff_pipe = StableDiffusionPipeline.from_pretrained(
    stable_diff_model,
    revision="fp16",
    torch_dtype=torch.float16,
    use_auth_token=authorization_token,
)
stable_diff_pipe.to(device)

# Load the text-to-video model
text_video_pipe = DiffusionPipeline.from_pretrained(
    "damo-vilab/text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16"
)
text_video_pipe.scheduler = DPMSolverMultistepScheduler.from_config(
    text_video_pipe.scheduler.config
)
text_video_pipe.enable_model_cpu_offload()

# Initialize the Flask app
app = Flask(__name__)
CORS(app)

# Set the base URL for the app
BASE_URL = os.getenv("BASE_URL", "http://localhost:5000")

# Create directories for generated images and videos
GENERATED_IMAGES_PATH = os.path.join(app.static_folder, "generated_images")
os.makedirs(GENERATED_IMAGES_PATH, exist_ok=True)

GENERATED_VIDEOS_PATH = os.path.join(app.static_folder, "generated_videos")
os.makedirs(GENERATED_VIDEOS_PATH, exist_ok=True)


# Define the routes
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/generate-image", methods=["POST"])
def generate_image():
    prompt = request.form.get("image-text")
    image_url = text_to_image_model(
        prompt, GENERATED_IMAGES_PATH, BASE_URL, device, stable_diff_pipe
    )
    return jsonify({"image_url": image_url})


@app.route("/generate-video", methods=["POST"])
def generate_video_route():
    prompt = request.form.get("video-text")
    video_url = text_to_video_model(
        prompt, GENERATED_VIDEOS_PATH, BASE_URL, device, text_video_pipe
    )
    return jsonify({"video_url": video_url})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
