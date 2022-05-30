from soupsieve import select
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda() :
    df_crime_pop = pd.read_csv('data/df_crime_pop.csv')
    df_crime_pop.columns = df_crime_pop.columns.str.replace(' ','') 

    st.dataframe(df_crime_pop)

    select_office = st.selectbox('관할서 선택',df_crime_pop['관서명'].to_list())

    if st.button('차트 확인') :
        ratio_jungbu = [136, 4, 3, 817, 3380]
        labels = ['강간','강도','살인','절도','폭력']
        colors = ['#9579D1', '#BE9DDF', '#FFA5D8', '#92DDEA', '#7EB8DA']
        wedgeprops={'width': 0.8, 'edgecolor': 'w', 'linewidth': 3}

        plt.pie(ratio_jungbu, labels=labels, labeldistance=1.2, autopct='%.0f%%', startangle=90, 
                counterclock=False, colors=colors, wedgeprops=wedgeprops)

        plt.legend(labels)

        plt.title('인천중부경찰서', size=14)

        plt.show()


