import streamlit as st
import math

from PIL import Image 


def run_home() :  
    st.title('인천광역시 5대 범죄 데이터')
    img = Image.open('data/police_st.PNG')
    st.image(img)
   
    st.subheader('위급상황을 위해 반드시 기억해야할 112 신고요령')
    video_file = open('data/emergency_112.mp4', 'rb')
    st.video(video_file)