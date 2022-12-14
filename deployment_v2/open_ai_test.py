import streamlit as st
import plotly.express as px

data = [1, 2, 3, 4]

chart = px.scatter(data, x=[1, 2, 3, 4], y=[1, 2, 3, 4])

st.markdown(
    """
    <div style="border: 2px solid red;">
        """ + chart.to_html(full_html=False) + """
    </div>
    """,
    unsafe_allow_html=True
)