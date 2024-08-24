# from diffusers import StableDiffusionPipeline, DDPMScheduler, UNet2DConditionModel
# from diffusers import AutoencoderKL, PNDMScheduler
# from torch.utils.data import DataLoader
# from transformers import CLIPTextModel
# import torch
# from torch.optim import AdamW
# from tqdm import tqdm
# from data_collection.download_datasets import prepare_coco_dataset

# coco_dataset = prepare_coco_dataset()

# # Load pre-trained components
# model_name = "CompVis/stable-diffusion-v1-4"
# text_encoder = CLIPTextModel.from_pretrained(model_name)
# vae = AutoencoderKL.from_pretrained(model_name)
# unet = UNet2DConditionModel.from_pretrained(model_name)

# # Setup pipeline
# pipeline = StableDiffusionPipeline.from_pretrained(
#     model_name, 
#     text_encoder=text_encoder,
#     vae=vae,
#     unet=unet,
#     scheduler=DDPMScheduler(num_train_timesteps=1000)
# )

# # Training setup
# train_dataloader = DataLoader(coco_dataset, batch_size=8, shuffle=True)
# optimizer = AdamW(pipeline.unet.parameters(), lr=5e-5)

# # Training loop
# for epoch in range(5):  # Adjust the number of epochs as necessary
#     for batch in tqdm(train_dataloader):
#         pixel_values = batch["pixel_values"].to(device)
#         input_ids = torch.tensor(batch["input_ids"]).to(device)

#         # Forward pass
#         loss = pipeline(pixel_values=pixel_values, input_ids=input_ids).loss
        
#         # Backward pass
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()

#     print(f"Epoch {epoch+1} completed. Loss: {loss.item()}")

# # Save the fine-tuned model
# pipeline.save_pretrained("fine-tuned-stable-diffusion")


