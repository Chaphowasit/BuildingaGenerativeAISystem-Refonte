import os
from flask import jsonify, request
from torch import autocast


# Define the text-to-image model
def text_to_image_model(prompt, GENERATED_IMAGES_PATH, BASE_URL, device, pipe):
    prompt = request.form.get("image-text")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    with autocast(str(device)):
        image = pipe(prompt, guidance_scale=8.5).images[0]

    image_filename = f"{prompt.replace(' ', '_')[:50]}.png"
    image_path = os.path.join(GENERATED_IMAGES_PATH, image_filename)
    image.save(image_path)

    image_url = f"{BASE_URL}/static/generated_images/{image_filename}"
    return image_url
