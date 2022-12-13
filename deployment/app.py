import streamlit as st
from streamlit_option_menu import option_menu
from pages import Pages
from charts_functions_compiled import charts
st.set_option('deprecation.showPyplotGlobalUse', False)

list_of_pages = [
    "Introduction",
    "EDA Findings",
    "Clusters and Results",
    "Model"
]

# Left the inside blank so that it really looks like a navbar
icons = ['building', 'chart_with_upwards_trend', 'circle', 'gear']
selection = option_menu("", list_of_pages, orientation='horizontal', icons=icons)

if selection == "Introduction":
    Pages.page_one()

elif selection == "EDA Findings":
    Pages.page_two()
    
elif selection == "Results":
    Pages.page_three()
    
elif selection == "Model":
    Pages.page_four()

