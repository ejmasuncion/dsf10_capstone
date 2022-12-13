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
from _4_classifier import *

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
st.set_page_config (layout="wide")



class Pages:
    
    def page_one():

        st.markdown("<h1 style='text-align: center'>Harnessing the Power of Data for Business Decisions in the Hotel Industry</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center'>Uplifting Philippine tourism by helping hotel owners improve service through a data-driven and customer centric approach</h3>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(" ")
        with col2:
            st.image("pictures/header_pic.jpg", width = 800)
        with col3:
            st.write(" ")
        
        
        st.markdown("")
        
        st.markdown("<h4 style='text-align: center'>DSF Cohort 10 Group 4", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center'>Andre | Andres | Enrico | Karen | Karla</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center'>Mentored by Ran</h4>", unsafe_allow_html=True)
        

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
        # charts.room_types() 
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
        col1, col2 = st.columns([1,1])

        with col1:
            st.markdown('Hotel Star Rating')
            choice_star = st.number_input("Choose one", 1, 5)
            st.markdown('Nationality')
            choice_nationality = st.selectbox("Choose One", ['Filipino', 'Foreigner'])
            st.markdown('Price')
            choice_price = st.number_input("Input Price")
            st.markdown('Entertainment Facilities')
            choice_ent = st.multiselect('Pick all applicable', ['restaurant', 'bar', 'swimming pool', 'fitness room', 'spa & wellness centre', 'garden'])
            st.markdown('Bedroom Amenities')
            choice_bed = st.multiselect('Pick all applicable', ['air conditioning', 'tv', 'linens', 'flat-screen tv', 'cable channels', 'telephone', 'electric kettle', 
                'slippers', 'wardrobe or closet', 'clothes rack', 'socket near the bed', 'refrigerator', 
                'satellite channels', 'terrace', 'soundproof rooms', 'safe'])
            st.markdown('Hotel Services')
            choice_ser = st.multiselect('Pick all applicable', ['airport shuttle', 'elevator', 'daily housekeeping', 'room service', 'baggage storage', 'laundry',
                'upper floors accessible by elevator', 'wake-up service', 'concierge', 'facilities for disabled guests', 'ironing service'])
            st.markdown('Number of Walkable Attractions')
            choice_loc = st.number_input("Input Number of Destinations", 1, 50)
            
        with col2:
            st.markdown('Occupant Type')
            choice_occupant = st.selectbox("Choose one", ["Solo Traveler", "Couple", "Family", "Group"])
            st.markdown('City')
            choice_city = st.text_input("Input City")
            st.markdown('Number of Nights')
            choice_nights = st.number_input("Input Number of Nights", 1, 50)
            st.markdown('Other Facilities')
            choice_other = st.multiselect('Pick all applicable', ['free parking', 'non-smoking rooms', 'designated smoking area', 'desk', 'smoke-free property', 
                   'meeting/banquet facilities', 'family rooms', 'facilities for disabled guests', 'business center'])
            st.markdown('Bathroom Amenities')
            choice_bath = st.multiselect('Pick all applicable', ['private bathroom', 'toilet', 'towels', 'free toiletries', 'shower', 'toilet paper', 
                 'bidet', 'hairdryer', 'bathtub or shower', 'bathrobe', 'hot tub/jacuzzi', 'dryer', 'raised toilet', 
                 'bathroom emergency cord'])
            st.markdown('Distance to nearest Airport')
            choice_airport = st.number_input("Input Distance")
            
        
        STA = int(choice_star)
        NAT = Classifier.get_nationality(choice_nationality)
        PRC = choice_price
        ENT = len(choice_ent)
        BDK = len(choice_bed)
        # SFK = len(choice_sec)
        OCT = Classifier.get_occupant(choice_occupant)
        LAT, LON = Classifier.get_lat_long(choice_city)
        NON = int(choice_nights)
        OTF = len(choice_other)
        BTK = len(choice_bath)
        SRK = len(choice_ser)
        CWA = int(choice_loc)
        TOP = float(NON*PRC)
        DNA = int(choice_airport)

        input_features = Classifier.input_features(STA, NAT, PRC, ENT, BDK, OCT, LAT, LON, NON, OTF, BTK, SRK, CWA, DNA, TOP)
        prediction = ''
        if st.button('Submit'):
            prediction = Classifier.model_fit(input_features)
        st.write(prediction)
