import numpy as np 
import pandas as pd 
import streamlit as st

import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import plotly as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

### ---------------------------------------
import warnings
warnings.filterwarnings('ignore')
import pickle
from _1_load_data import Load_Data
from _2_visuals import Graphs
from _2_chart_functions import Chart_Functions

### ---------------------------------------
dl=Load_Data()
cf=Chart_Functions()
g=Graphs()

df_og=dl.pp_raw_hotel_data()
### ---------------------------------------
from charts_functions_compiled import charts

'''
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', '{:,.5f}'.format)
'''


pd.set_option('display.float_format', '{:,.2f}'.format)
st.set_option('deprecation.showPyplotGlobalUse', False)

# Setting general format to the graphs
sns.set_theme(style="white", font="sans-serif")
st.set_page_config (layout="wide",
)



class Pages:
    
    def page_one():
        st.markdown("<h1 style='text-align: center'>TRAVEL LOG</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center'>Harnessing the Power of Data for Business Decisions in the Hotel Industry</h3>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.write('')
        
        with col2:
            image_path = "pictures/header_pic.jpg"
            st.image(image_path)
            
        with col3:
            st.write('')
        
        
        # st.markdown("<h4 style='text-align: center'>Andre | Andres | Enrico | Karen | Karla</h4>", unsafe_allow_html=True)
        

    # Page 2 - "Big News for Zack!
    def page_two():
        # Write the title
        st.title(
            "EDA Findings"
        )
        st.caption(
            "Testing caption")
            
        subheader = '<p style="font-family:Arial; font-size: 40px; text-align: left;">Sample text <b>in HTML</b></p>'
        st.markdown(subheader, unsafe_allow_html=True)
        
    def page_three():
        st.title(
            "Results"
        )
        
        
        
    
        # time_series_initial
        # local_vs_foreign
        # room_types
        # occupant_types
        # nights_stayed
        # time_series_month
        # time_series_year
        # wordcloud - doesn't print yet
        # quality_and_stars - doesn't print yet
        # facilities_positive
        # facilities_negative
        
        charts.time_series_initial() 
        st.write("time_series_initial")
        charts.local_vs_foreign() 
        st.write("local_vs_foreign")
        charts.room_types() 
        # st.write("room_types")
        # charts.occupant_types() 
        # st.write("occupant_types")
        # charts.nights_stayed() 
        # st.write("nights_stayed")
        # charts.time_series_month() 
        # st.write("time_series_month")
        # charts.time_series_month() 
        # st.write("time_series_year")
        # charts.wordcloud() 
        # st.write("wordcloud")
        # charts.quality_and_stars() 
        # st.write("quality_and_stars")
        # charts.facilities_positive() 
        # st.write("facilities_positive")
        # charts.facilities_negative() 
        # st.write("facilities_negative")
        
    def page_four():
        st.title(
            "The Model"
        )