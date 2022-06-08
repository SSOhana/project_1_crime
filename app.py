import streamlit as st
import pandas as pd
from app_eda import run_eda
from app_home import run_home


def main() :
    
    menu = ['Home', 'EDA']
    choice = st.sidebar.selectbox('메뉴 선택', menu)



    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_eda()




if __name__ == '__main__' :
    main()