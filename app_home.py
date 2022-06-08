import streamlit as st
import math
import pandas as pd

from geopy.geocoders import Nominatim
import geopy.distance

from streamlit_folium import st_folium
import folium as g

from PIL import Image 


def run_home() :  
    st.title('인천경찰청 위치 및 범죄 데이터')
    img = Image.open('data/police_st.PNG')
    st.image(img)
   
    st.subheader('인천광역시 관할 경찰서 위치')
    st.info('우리 동네 경찰서 위치를 확인해보세요.')

    
    # 지도
    police_loc = pd.read_csv('data/police_loc.csv')
    pd.options.display.float_format = '{: .14f}'.format

    # 위도
    latitude = 37.4727937
    # 경도
    longitude = 126.6225932

    m = g.Map(location=[latitude, longitude],
               zoom_start=11)

    police_loc.reset_index(inplace=True)
    for i in range(len(police_loc)) :
        marker01 = g.Marker([police_loc.loc[i]['위도'], police_loc.loc[i]['경도']],
                            popup = police_loc.loc[i]['관서명'],
                            icon=g.Icon('blue', icon='star')) 
        marker01.add_to(m)

    st_data = st_folium(m, width=800)


    # 신고요령 동영상
    st.subheader('위급상황을 위해 반드시 기억해야할 112 신고요령')
    st.info('신고 요령을 터득하여 보다 신속하게 도움을 받아보세요.')
    video_file = open('data/emergency_112.mp4', 'rb')
    st.video(video_file)





