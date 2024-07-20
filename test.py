# import requests

# def generate_image_from_api(prompt):
#     url = "http://localhost:8000/generate_image"
#     response = requests.post(url, json={"prompt": prompt})
#     if response.status_code == 200:
#         with open("output.png", "wb") as f:
#             f.write(response.content)
#         return True
#     else:
#         return False

# generate_image_from_api('ugly cat')

import subprocess

prompt = 'ugly cat'
command = f"/home/intern/Downloads/internsproject/stable-diffusion.cpp/build/bin/sd -m /home/intern/Downloads/internsproject/stable-diffusion.cpp/models/FluentlyXL-Final.safetensors --vae /home/intern/Downloads/internsproject/stable-diffusion.cpp/models/sdxl_vae.safetensors -H 256 -W 256 -p \'{prompt}\'"
subprocess.run(command, shell=True)