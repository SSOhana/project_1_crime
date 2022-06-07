import streamlit as st
import math
import pandas as pd

from geopy.geocoders import Nominatim
import geopy.distance

from streamlit_folium import st_folium
import folium as g

from PIL import Image 


def run_home() :  
    st.title('인천광역시 5대 범죄 데이터')
    img = Image.open('data/police_st.PNG')
    st.image(img)
   


    #지도
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

    st_data = st_folium(m, widht = 725)





    st.subheader('위급상황을 위해 반드시 기억해야할 112 신고요령')
    video_file = open('data/emergency_112.mp4', 'rb')
    st.video(video_file)






    # geo_local = Nominatim(user_agent='South Korea')

    #     # 위도, 경도 반환하는 함수
    # def geocoding(address):
    #     geo = geo_local.geocode(address)
    #     x_y = [geo.latitude, geo.longitude]
    #     return x_y
        



    # incheon_address = ['대한민국 인천광역시 중구 항동2가 2-7', '대한민국 인천광역시 남구 매소홀로290번길 32',
    # '대한민국 인천광역시 남동구 구월1동 1447-2', '대한민국 인천광역시 부평구 길주로 511',
    # '대한민국 인천광역시 서구 심곡동 281-2', '대한민국 인천광역시 계양구 계산새로',
    # '대한민국 인천광역시 강화군 강화읍 관청리 437', '대한민국 인천광역시 연수구 연수2동 원인재로 138',
    # '대한민국 인천광역시 부평구 삼산동 441-1', '대한민국 인천광역시 남동구 논현2동 363-4',
    # '대한민국 인천광역시 남구 매소홀로290번길 32']
    

    # for i in incheon_address :
    #     lat_01 = geocoding(i)[0]
    #     lng_01 = geocoding(i)[1]
    #     # st.text('첫번째 장소의 위도 : {}, 경도 : {}'.format(lat_01,lng_01))
            
    #     map_data = pd.DataFrame({'latitude':[lat_01],'longitude':[lng_01]})
        
    # st.map(data= map_data, zoom = 9)
    