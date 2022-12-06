import streamlit as st
from streamlit_option_menu import option_menu
from pages import Pages
from flask import Flask
from flask.templating import render_template

def index():
    return render_template('index.html', name='home')
    

list_of_pages = [
    "Testing 1",
    "Testing 2"
]

#st.sidebar.title('Breaking into the US! :notes:')
#st.sidebar.markdown('by Group Mic :microphone: | DSFC10')
selection = option_menu("Go to: ", list_of_pages, orientation='horizontal')

if selection == "Testing 1":
    Pages.page_one()

elif selection == "Testing 2":
    Pages.page_two()
