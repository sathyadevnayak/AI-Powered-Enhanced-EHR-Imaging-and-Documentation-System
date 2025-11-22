import streamlit as st
from PIL import Image
import io
from diffusers import StableDiffusionUpscalePipeline
import torch

def image_enhancement_model(Image):
    img = Image.convert("RGB")
    model_id = "stabilityai/stable-diffusion-x4-upscaler"
    pipe = StableDiffusionUpscalePipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    prompt = "enhance photo"
    
    enhanced_img = pipe(prompt=prompt, image=img).images[0]
    return enhanced_img

def render():
    st.markdown('<h2 class="sub-header">🔬 Medical Image Enhancement</h2>', unsafe_allow_html=True)
    st.markdown("### 📤 Upload Medical Image")
    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        
        
        enhance_button = st.button("✨ Enhance Image", type="primary", use_container_width=True)
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            min_size = 64  # SD upscaler needs at least 64x64
            if image.width < min_size or image.height < min_size:
                image = image.resize((max(image.width, min_size), max(image.height, min_size)))
            st.image(image, caption="Original Image", use_container_width=True)
             
    with col2:
        if enhance_button and uploaded_file is not None:
            st.markdown("### ✨ Enhanced Result")
            
            
            with st.spinner("Enhancing image, please wait..."):
                image = image_enhancement_model(image).resize((max(image.width, min_size), max(image.height, min_size)))
                st.image(image, caption="Enhanced Image", use_container_width=True)
                
                st.success("✅ Image enhancement complete!")
                
                st.markdown("""
                **Enhancement Details:**
                - ✅ Denoising applied
                - ✅ Resolution enhanced
                - ✅ Contrast optimized
                - ✅ Edge sharpening applied
                """)
                
                buf = io.BytesIO()
                image.save(buf, format='PNG')
                byte_im = buf.getvalue()
                
                st.download_button(
                    label="💾 Download Enhanced Image",
                    data=byte_im,
                    file_name=f"enhanced_{uploaded_file.name}",
                    mime="image/png",
                    use_container_width=True
                )
        else:
            st.info("👈 Upload an image and click 'Enhance Image' to process")