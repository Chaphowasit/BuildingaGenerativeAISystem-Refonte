import os
from PIL import Image
from torchvision import transforms
from transformers import AutoTokenizer


def prepare_coco_dataset():
    # Load the tokenizer if needed (skip this if not using a tokenizer)
    #  tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

    # Define paths and image transformations
    image_path = "data/coco/train2017/000000000009.jpg"  # Use a specific image ID

    image_transform = transforms.Compose(
        [
            transforms.Resize((256, 256)),  # Resize to 256x256
            transforms.ToTensor(),
            transforms.Normalize([0.5], [0.5]),  # Normalize to [-1, 1]
        ]
    )

    def preprocess_image(image_path):
        # Load and transform the image
        image = Image.open(image_path).convert("RGB")
        pixel_values = image_transform(image)
        return {"pixel_values": pixel_values}

    # Preprocess the single image
    print("Loading and processing the image...")
    processed_image = preprocess_image(image_path)
    print("Image processed.")

    return processed_image


# Example usage
coco_dataset = prepare_coco_dataset()
