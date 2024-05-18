import streamlit as st
from rembg import remove
from PIL import Image
import io
import time

st.header("Background Remover")
input_img = st.file_uploader(label="Upload your image", type=["png", "jpg", "jpeg", "webp"])

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

    progress_bar.empty()
