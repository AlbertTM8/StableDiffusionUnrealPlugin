from diffusers import AutoPipelineForInpainting
from diffusers.utils import load_image
import torch

from PIL import Image, ImageDraw
import numpy as np


def circle_mask(img):
    """Roll the images 50% vertical and horz and mask the new center for in-fill"""
    w, h = img.size
    x = np.roll(np.roll(np.array(img), h // 2, 0), w // 2, 1)

    img2 = Image.fromarray(x)
    mask = Image.fromarray(np.zeros_like(x)[:, :, 0])

    draw = ImageDraw.Draw(mask)
    coords = [(w / 2, 0), (w, h / 2), (w / 2, h), (0, h / 2)]
    draw.polygon(coords, fill=255)

    return img2, mask


def generate_inpainting(input_prompt, input_img, input_msk):
    image = Image.open("/home/albert/seamlesstexturegen/seamlessgen/9f231d873ce310a5f9dc461a22893aa074b8039080908c94d18837f7.jpg")
    output_img, output_msk = circle_mask(image)
    prompt = input_prompt

    pipe = AutoPipelineForInpainting.from_pretrained("diffusers/stable-diffusion-xl-1.0-inpainting-0.1", torch_dtype=torch.float16, variant="fp16").to("cuda")

    image = output_img.resize((1024, 1024))
    mask_image = output_msk.resize((1024, 1024))

    prompt = "wood texture"
    generator = torch.Generator(device="cuda").manual_seed(0)

    image = pipe(
    prompt=prompt,
    image=image,
    mask_image=mask_image,
    guidance_scale=8.0,
    num_inference_steps=20,  # steps between 15 and 30 work well for us
    strength=0.99,  # make sure to use `strength` below 1.0     
    generator=generator,
    ).images[0]
    image.save("./" + prompt + ".png")