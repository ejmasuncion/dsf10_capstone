import pandas as pd
import seaborn as sns
import streamlit as st
import numpy as np

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
