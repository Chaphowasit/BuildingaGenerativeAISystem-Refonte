import os
import numpy as np
import imageio
import torch
from torch import autocast


def text_to_video_model(prompt, GENERATED_VIDEOS_PATH, BASE_URL, device, pipe):
    video_frames = pipe(prompt, num_inference_steps=20).frames
    # Convert frames to RGB only if necessary
    rgb_frames = []
    for batch in video_frames:
        for frame in batch:
            frame = np.array(frame)
            # Perform channel check only if absolutely necessary
            if frame.ndim == 2 or frame.shape[-1] == 1:
                frame = (
                    np.stack([frame] * 3, axis=-1)
                    if frame.ndim == 2
                    else np.concatenate([frame] * 3, axis=-1)
                )
            rgb_frames.append(
                (frame * 255).astype(np.uint8)
            )  # Convert frame to uint8 for imageio

    # Generate video file path and save
    video_filename = f"{prompt.replace(' ', '_')[:50]}.mp4"
    video_path = os.path.join(GENERATED_VIDEOS_PATH, video_filename)

    # Write the video in a single step, reducing multiple I/O operations
    try:
        imageio.mimsave(video_path, rgb_frames, fps=30)
        video_url = f"{BASE_URL}/static/generated_videos/{video_filename}"
        return video_url
    except ValueError as e:
        print(f"An error occurred: {e}")
        return None
