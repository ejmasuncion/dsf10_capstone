import streamlit as st
from streamlit_option_menu import option_menu
from pages import Pages
from charts_functions_compiled import charts

list_of_pages = [
    "Testing 1",
    "Testing 2",
    "Charts Dump"
]

st.write("test")

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

charts.facilities_positive() 

# Left the inside black so that it really looks like a navbar
selection = option_menu("", list_of_pages, orientation='horizontal')

if selection == "Testing 1":
    Pages.page_one()

elif selection == "Testing 2":
    Pages.page_two()
    
elif selection == "Charts Dump":
    Pages.page_three()
    
