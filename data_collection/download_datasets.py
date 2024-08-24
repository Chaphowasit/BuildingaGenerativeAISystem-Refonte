# data_collection/download_datasets.py
import os
import requests
import zipfile
from datasets import load_dataset
from transformers import CLIPTokenizer
from PIL import Image
import torch
from torchvision import transforms

def download_coco_dataset():
    url = "http://images.cocodataset.org/zips/train2017.zip"
    output_dir = "data/coco"
    os.makedirs(output_dir, exist_ok=True)
    
    response = requests.get(url)
    with open(os.path.join(output_dir, "train2017.zip"), "wb") as file:
        file.write(response.content)

    with zipfile.ZipFile(os.path.join(output_dir, "train2017.zip"), 'r') as zip_ref:
        zip_ref.extractall(output_dir)
        
def prepare_coco_dataset():
    download_coco_dataset()
    # Define paths
    data_dir = "data/coco/train2017/"
    # Load COCO annotations (captions)
    coco_dataset = load_dataset("coco", split="train")
    # Tokenizer
    tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-large-patch14")
    # Define image transformations
    image_transform = transforms.Compose([
        transforms.Resize((512, 512)),
        transforms.ToTensor(),
        transforms.Normalize([0.5], [0.5]),  # Normalize between [-1, 1]
    ])

    def preprocess_data(example):
        # Load and transform the image
        image_path = os.path.join(data_dir, f"{example['image_id']:012d}.jpg")
        image = Image.open(image_path).convert("RGB")
        example['pixel_values'] = image_transform(image)
        
        # Tokenize the captions
        example['input_ids'] = tokenizer(example['caption'], max_length=77, padding="max_length", truncation=True).input_ids
        return example
    
    coco_dataset = coco_dataset.map(preprocess_data)
    return coco_dataset


# def download_tdiuc_dataset():
#     url = "http://www.tdiucdataset.org/download/tdiuc.zip"
#     output_dir = "data/tdiuc"
#     os.makedirs(output_dir, exist_ok=True)

#     response = requests.get(url)
#     with open(os.path.join(output_dir, "tdiuc.zip"), "wb") as file:
#         file.write(response.content)

#     with zipfile.ZipFile(os.path.join(output_dir, "tdiuc.zip"), 'r') as zip_ref:
#         zip_ref.extractall(output_dir)

# if __name__ == "__main__":
#     prepare_coco_dataset()
#     download_tdiuc_dataset()
