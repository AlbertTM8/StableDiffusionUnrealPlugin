from diffusers import DiffusionPipeline
import torch
import numpy as np
from PIL import Image, ImageDraw

# def tensor_to_image(tensor):
#     tensor = tensor * 255
#     tensor = tensor.byte()  # Convert to 8-bit integer
#     tensor = tensor.permute(1, 2, 0)  # Change [C, H, W] to [H, W, C]
#     return PIL.Image.fromarray(tensor)

def generate_image():
    base = DiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, variant="fp16", use_safetensors=True
    )
    base.to("cuda")
    refiner = DiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-refiner-1.0Asddasd",
        text_encoder_2=base.text_encoder_2,
        vae=base.vae,
        torch_dtype=torch.float16,
        use_safetensors=True,
        variant="fp16",
    )
    refiner.to("cuda")

    # Define how many steps and what % of steps to be run on each experts (80/20) here
    n_steps = 40
    high_noise_frac = 0.8

    prompt = "A majestic lion jumping from a big stone at night"

    # run both experts
    image = base(
        prompt=prompt,
        num_inference_steps=n_steps,
        denoising_end=high_noise_frac,
        output_type="latent",
    ).images
    image = refiner(
        prompt=prompt,
        num_inference_steps=n_steps,
        denoising_start=high_noise_frac,
        image=image,
    ).images[0]

if __name__ == "__main__":
    generate_image()


