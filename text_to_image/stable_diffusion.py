from parti_pytorch import VitVQGanVAE, VQGanVAETrainer, Parti
import torch
from download_datasets import coco_dataset
from torch.utils.data import DataLoader
from PIL import Image

# Ensure coco_dataset is loaded properly and has data
print(coco_dataset)
print(f"Number of samples in dataset: {len(coco_dataset)}")
print("Downloaded COCO dataset")

# Initialize and train the VQ-GAN VAE
vit_vae = VitVQGanVAE(dim=256, image_size=256, patch_size=16, num_layers=3)

# Prepare DataLoader
dataloader = DataLoader(
    coco_dataset,
    batch_size=1,  # Adjust based on your memory and dataset size
    shuffle=True,
    num_workers=4,  # Adjust based on your system
)

trainer = VQGanVAETrainer(
    vit_vae,
    folder="data/coco/train2017/",  # Path to your COCO images
    num_train_steps=100000,
    lr=3e-4,
    batch_size=1,
    grad_accum_every=8,
    amp=False,  # Disabled AMP for CPU
)

trainer.train()
print("Trained VQ-GAN VAE")

# Save the trained VAE model
torch.save(vit_vae.state_dict(), "vit_vae.pt")

# Load the trained VQ-GAN VAE model
vit_vae = VitVQGanVAE(dim=256, image_size=256, patch_size=16, num_layers=3)
vit_vae.load_state_dict(torch.load("vit_vae.pt", map_location=torch.device("cpu")))

# Initialize the Parti model with the trained VAE
parti = Parti(
    vae=vit_vae,
    dim=512,
    depth=8,
    dim_head=64,
    heads=8,
    dropout=0.0,
    cond_drop_prob=0.25,
    ff_mult=4,
    t5_name="t5-large",
)

# Example training loop with preprocessed data
for batch in dataloader:  # Assuming dataloader provides batches of data
    images = batch["pixel_values"]  # Tensor images
    texts = batch["caption"]  # Texts associated with images

    # Ensure images and texts are properly formatted
    images = images.to(torch.device("cpu"))
    texts = texts  # Assuming texts are already in the correct format

    loss = parti(texts=texts, images=images, return_loss=True)
    loss.backward()

    # Perform optimizer step (you need to define the optimizer and step here)
    # optimizer.step()
    # optimizer.zero_grad()

print("Trained Parti model")

# Generate images from text prompts using the trained Parti model
generated_images = parti.generate(
    texts=[
        "a whale breaching from afar",
        "young girl blowing out candles on her birthday cake",
        "fireworks with blue and green sparkles",
    ],
    cond_scale=3.0,
    return_pil_images=True,
)

print("Generated images")
# Display the generated images
for img in generated_images:
    img.show()
