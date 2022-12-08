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

'''
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', '{:,.5f}'.format)
'''


pd.set_option('display.float_format', '{:,.2f}'.format)

# Setting general format to the graphs
sns.set_theme(style="white", font="sans-serif")
st.set_page_config (layout="wide")



class Pages:
    
    # Page 1 - "The Project"
    def page_one():
    # Write the title and the subheader
        st.title(
            "Testing page"
        )
        st.subheader(
            'Capstone Group 4'
            )
        st.markdown('Andre | Andres | Enrico | Karen | Karla')
        st.markdown('Test page')

        

    # Page 2 - "Big News for Zack!
    def page_two():
        # Write the title
        st.title(
            "Another testing page"
        )
        st.caption(
            "Testing caption")
            
        subheader = '<p style="font-family:Arial; font-size: 40px; text-align: left;">Sample text <b>in HTML</b></p>'
        st.markdown(subheader, unsafe_allow_html=True)
        
    def page_three():
        st.title(
            "Charts Dump, Unformatted"
        )
        
