import subprocess
import streamlit as st
import torch

# Load the model and tokenizer
model_id = "fluently/Fluently-XL-Final"
device = "cuda" if torch.cuda.is_available() else "cpu"


# Streamlit interface
st.markdown("<h3 style='text-align: center;'>Text-to-Image Generation</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter a prompt to generate an image</p>", unsafe_allow_html=True)
# st.subheader("Text-to-Image Generation")
# Input prompt from user
col1, col2 = st.columns(2)

# Input field 1
with col1:
    height = st.number_input("Height", min_value=64, step=640)
# Input field 2
with col2:
    width = st.number_input("Width", min_value=64, step=640)
user_input = st.text_input("Prompt", "")

# Submit button
if st.button("Generate"):
    if user_input:
        with st.spinner("Generating image..."):
            # Generate the image
            prompt = user_input
            command = f"C:\Users\udaiy\Downloads\internsproject\stable-diffusion.cpp\build\bin\sd -m C:\Users\udaiy\Downloads\internsproject\stable-diffusion.cpp\models\FluentlyXL-Final.safetensors --vae C:\Users\udaiy\Downloads\internsproject\stable-diffusion.cpp\models\sdxl_vae.safetensors -H {height} -W {width} -p \'{prompt}\'"
            subprocess.run(command, shell=True)
            image = 'output.png'
            # Display the image
            st.image(image, caption=user_input)
    else:
        st.write("Please enter a prompt.")

# To run the app, use the command: streamlit run streamlit_app_cpp.py
