from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from dotenv import load_dotenv
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

# from dotenv import load_dotenv

# load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
CORS(app)  # Enable CORS

# Base URL for serving images
BASE_URL = os.getenv(
    "BASE_URL", "http://localhost:5000"
)  # Default to localhost for development

# Path to save generated images
GENERATED_IMAGES_PATH = os.path.join(app.static_folder, "generated_images")
os.makedirs(GENERATED_IMAGES_PATH, exist_ok=True)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


def load_image_generator_model(device):
    authorization_token = os.getenv("AUTH_TOKEN", "")
    model_id = "CompVis/stable-diffusion-v1-4"
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        revision="fp16",
        torch_dtype=torch.float16,
        use_auth_token=authorization_token,
    )
    pipe.to(device)
    return pipe


@app.route("/generate-image", methods=["POST"])
def generate_image():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # Get prompt from the frontend form
    prompt = request.form.get("image-text")  # Changed to 'image-text'
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    # Load the model
    pipe = load_image_generator_model(device)
    # Generate the image
    with autocast(str(device)):
        image = pipe(prompt, guidance_scale=8.5).images[0]
    # Save the image
    image_filename = f"{prompt.replace(' ', '_')[:50]}.png"  # Limit filename length
    image_path = os.path.join(GENERATED_IMAGES_PATH, image_filename)
    image.save(image_path)
    # Return the image URL
    image_url = f"{BASE_URL}/static/generated_images/{image_filename}"
    return jsonify({"image_url": image_url})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
