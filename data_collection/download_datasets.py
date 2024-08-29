# import os
# import requests
# import zipfile
# from PIL import Image
# from torchvision import transforms
# from datasets import load_dataset
# import torch


# def download_coco_dataset():
#     url = "http://images.cocodataset.org/zips/train2017.zip"
#     output_dir = "data/coco"
#     os.makedirs(output_dir, exist_ok=True)

#     response = requests.get(url)
#     with open(os.path.join(output_dir, "train2017.zip"), "wb") as file:
#         file.write(response.content)

#     with zipfile.ZipFile(os.path.join(output_dir, "train2017.zip"), "r") as zip_ref:
#         zip_ref.extractall(output_dir)


# def prepare_coco_dataset():
#     # download_coco_dataset()
#     print("hi0")
#     # Load COCO annotations (captions)
#     coco_dataset = load_dataset("coco", split="train", cache_dir="data/coco")
#     print("hi1")
#     # Define paths and image transformations
#     data_dir = "data/coco/train2017/"
#     image_transform = transforms.Compose(
#         [
#             transforms.Resize((256, 256)),  # Change to 256x256
#             transforms.ToTensor(),
#             transforms.Normalize([0.5], [0.5]),  # Normalize between [-1, 1]
#         ]
#     )

#     def preprocess_data(example):
#         # Load and transform the image
#         image_path = os.path.join(data_dir, f"{example['image_id']:012d}.jpg")
#         image = Image.open(image_path).convert("RGB")
#         example["pixel_values"] = image_transform(image)

#         # Tokenize the captions (if needed for VAE training)
#         # Replace tokenizer logic according to your model's tokenizer if needed
#         example["input_ids"] = tokenizer(
#             example["caption"], max_length=77, padding="max_length", truncation=True
#         ).input_ids
#         return example

#     print("hi2")
#     coco_dataset = coco_dataset.map(preprocess_data)
#     return coco_dataset


# coco_dataset = prepare_coco_dataset()
