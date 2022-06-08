from soupsieve import select

import streamlit as st               # 스트림릿 라이브러리
import pandas as pd
import numpy as np

import matplotlib
# matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

from PIL import Image 


# 한글 깨짐 현상시 사용하는 코드
import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')
    
# import platform

# from matplotlib import font_manager, rc
# plt.rcParams['axes.unicode_minus'] = False

# if platform.system() == 'Linux':
#     rc('font', family='AppleGothic')
# elif platform.system() == 'Windows':
#     path = "c:/Windows/Fonts/malgun.ttf"
#     font_name = font_manager.FontProperties(fname=path).get_name()
#     rc('font', family=font_name)
# else:
#     print('Unknown system... sorry~~~~')




def run_eda() :
    st.title('인천광역시 범죄 신고 건수 데이터')
    st.info('중구,동구,옹진은 중부서에 포함되어있습니다.')

    df_crime_pop = pd.read_csv('data/df_crime_pop.csv')
    df_crime_pop.columns = df_crime_pop.columns.str.replace(' ','') 

    with st.expander('인천광역시 5대 범죄 신고건수와 인구수 표확인하기') :
         st.dataframe(df_crime_pop)


    # 차트1 : 인구 천명당 범죄 신고 비율
    st.subheader('인구 대비 범죄 신고 건수')
    st.info('인구수 대비 범죄 신고 건수로 작성된 차트입니다.')

    # img2 = Image.open('data/chart.png')
    # st.image(img2)

    group_crime_pop = pd.read_csv('data/group_crime_pop.csv')

    # 차트 데이터 가공
    mc = group_crime_pop.loc[:, '5대범죄'][0] / group_crime_pop.loc[:, '인구수'][0] * 1000
    gh = group_crime_pop.loc[:, '5대범죄'][1] / group_crime_pop.loc[:, '인구수'][1] * 1000
    gy = group_crime_pop.loc[:, '5대범죄'][2] / group_crime_pop.loc[:, '인구수'][2] * 1000
    nd = group_crime_pop.loc[:, '5대범죄'][3] / group_crime_pop.loc[:, '인구수'][3] * 1000
    bp = group_crime_pop.loc[:, '5대범죄'][4] / group_crime_pop.loc[:, '인구수'][4] * 1000
    sg = group_crime_pop.loc[:, '5대범죄'][5] / group_crime_pop.loc[:, '인구수'][5] * 1000
    ys = group_crime_pop.loc[:, '5대범죄'][6] / group_crime_pop.loc[:, '인구수'][6] * 1000
    jg = group_crime_pop.loc[:, '5대범죄'][7] / group_crime_pop.loc[:, '인구수'][7] * 1000


    ratio = [mc, gh, gy, nd, bp, sg, ys, jg]
    labels = group_crime_pop['구 별']
    colors = ['#9579D1', '#BE9DDF', '#FFA5D8', '#92DDEA', '#7EB8DA','#FFCBCB', '#7BCABF', '#FF9797']
    wedgeprops={'width': 0.8, 'edgecolor': 'w', 'linewidth': 3}

    # with st.expander('chart') :

    fig1 = plt.figure() 
    plt.pie(ratio, labels=labels, labeldistance=1.2, autopct='%.0f%%', startangle=90, 
            counterclock=False, colors=colors, wedgeprops=wedgeprops)
    plt.legend(loc=(-0.5,0.2))
    plt.title('인구 천명당 범죄 신고 건수 비율', size=14)

    st.pyplot(fig1)

    if st.checkbox('구 별 인구수와 5대 범죄 신고 건수 데이터 표 보기') :
        st.dataframe(group_crime_pop)
    else :
        st.text('데이터 숨김')



    # 관서별 인구수 및 범죄 신고건수
    st.subheader('연관성 확인')
    st.info('연관성을 확인하고 싶은 항목을 선택해주세요.')
    
    df_crime_pop.drop(['관서명','구별'], axis=1).columns.to_list()
    multi1 = st.multiselect('항목 선택', df_crime_pop.drop(['관서명','구별'], axis=1).columns.to_list())

    if st.button('연관성 확인') :

        #fig2 = plt.figure() // 이 방법으로 안될 때가 있어서 아래 코드로!!
        fig2 = sns.pairplot(data=df_crime_pop, vars=df_crime_pop[multi1])

        st.pyplot(fig2)













    # if st.button('차트 확인') :
    #   st.dataframe(df_crime_pop)  # 이 부분 히스토그램으로 바꿔줘야..!!



