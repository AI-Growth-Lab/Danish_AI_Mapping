#Import libraries
import folium
import branca
import pandas as pd
import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from folium.plugins import Draw
from streamlit_folium import st_folium

def intro():
    st.write("# Welcome to Danish AI Mapping! 👋")

    st.markdown(
        """
Danish AI Mapping is an app built specifically for landscaping AI companies in Denmark.

        """
    )

intro()




