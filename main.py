import subprocess
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

class ImageRequest(BaseModel):
    prompt: str

def generate_image(image_request: ImageRequest):
    try:
        prompt = image_request.prompt
        command = f"C:\Users\udaiy/Downloads/internsproject/stable-diffusion.cpp/build/bin/sd -m C:\Users\udaiy/Downloads/internsproject/stable-diffusion.cpp/models/FluentlyXL-Final.safetensors --vae C:\Users\udaiy/Downloads/internsproject/stable-diffusion.cpp/models/sdxl_vae.safetensors -H 256 -W 256 -p \'{prompt}\'"
        subprocess.run(command, shell=True)  # Replace with more robust process management for production
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

@app.post("/generate_image")
async def generate_image_endpoint(prompt: str):
    image_path = generate_image(prompt)  # Assuming image is saved as 'output.png'
    return FileResponse(image_path)