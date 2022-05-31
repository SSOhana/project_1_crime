from soupsieve import select

import streamlit as st               # 스트림릿 라이브러리
import pandas as pd
import numpy as np

import matplotlib
# matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns



# 한글 깨짐 현상시 사용하는 코드
import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')
#



def run_eda() :
    st.title('인천광역시 5대 범죄 데이터')
    st.text('중구,동구,옹진은 중부서에 포함되어있습니다.')

    df_crime_pop = pd.read_csv('data/df_crime_pop.csv')
    df_crime_pop.columns = df_crime_pop.columns.str.replace(' ','') 

    st.dataframe(df_crime_pop)


    # 차트1 : 범죄별
    st.text('인구수 대비 신고율이 아닌 각 서 별 범죄 신고율로만 작성된 차트입니다.')
    select_office = st.selectbox('범죄 선택',df_crime_pop.columns[1:6].to_list())
    print(select_office)


    if st.button('차트 확인') :

        ratio_office = df_crime_pop[select_office]
        labels = df_crime_pop['관서명']
        colors = ['#9579D1', '#BE9DDF', '#FFA5D8', '#92DDEA', '#7EB8DA','#FFCBCB', '#7BCABF', '#586FAB', '#93B3B7', '#FF9797']
        wedgeprops={'width': 0.8, 'edgecolor': 'w', 'linewidth': 3}

        fig1 = plt.figure() 
        plt.pie(ratio_office, labels=labels, labeldistance=1.2, autopct='%.0f%%', startangle=90, 
                counterclock=False, colors=colors, wedgeprops=wedgeprops)
        plt.legend(loc=(-1,0.2))
        plt.title(select_office, size=14)

        st.pyplot(fig1)

        