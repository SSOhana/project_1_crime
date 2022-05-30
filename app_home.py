import streamlit as st
from PIL import Image 

def run_home() :  
    img = Image.open('data/incheon_police.png')
    st.image(img)