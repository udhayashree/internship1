import torch
from diffusers import StableDiffusionXLPipeline
from PIL import Image

# Set the device to CPU
device = "cpu"

# Load the model
model_id = "fluently/Fluently-XL-Final"
pipe = StableDiffusionXLPipeline.from_pretrained(model_id, torch_dtype=torch.float32).to(device)

# Define the text prompt
prompt = "Cleopatra standing in front of the pyramids of Giza."

# Generate the image
image = pipe(prompt, num_inference_steps=30, guidance_scale=7.5).images[0]

# Display the image
image.show()