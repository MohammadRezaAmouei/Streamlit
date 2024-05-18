import streamlit as st
from rembg import remove
from PIL import Image
import io
import time
import base64

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

def get_image_download_link(img, filename, text):
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/png;base64,{img_str}" download="{filename}">{text}</a>'
    return href

st.markdown("<h1>Background Remover</h1>", unsafe_allow_html=True)
input_img = st.file_uploader(label="", type=["png", "jpg", "jpeg", "webp"])

if input_img is not None:
    img_bytes = input_img.read()
    original_image = Image.open(io.BytesIO(img_bytes))
    
    progress_bar = st.progress(0)
    
    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)
    
    processed_img = remove(img_bytes)
    processed_image = Image.open(io.BytesIO(processed_img))

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original Image")
        st.image(original_image, use_column_width=True)
    with col2:
        st.subheader("Background Removed")
        st.image(processed_image, use_column_width=True)
        st.markdown(get_image_download_link(processed_image, "processed_image.png", "Download Processed Image"), unsafe_allow_html=True)

    progress_bar.empty()
