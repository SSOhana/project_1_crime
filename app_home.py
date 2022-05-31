import streamlit as st
from PIL import Image 

def run_home() :  
    st.title('인천광역시 5대범죄')

    img = Image.open('data/emergency.jpg')
    st.image(img)