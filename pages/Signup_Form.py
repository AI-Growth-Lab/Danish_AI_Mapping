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


def signup_form():
    st.write("# Welcome to Danish AI Mapping!")

    st.markdown(
        """
Danish AI Mapping is an app built specifically for landscaping AI companies in Denmark.

        """
    )
    df_template = pd.DataFrame(
    '',
    index=range(10),
    columns=list('abcde'))
    st.subheader("Create New Profile for Your Company")
    startup_name = st.text_input("Company Name")
    startup_url = st.text_input("Company URL")
    startup_founding_year = st.text_input("Company Founding Year")
    city_state = st.text_input("City")
    address_street = st.text_input("Street")
    address_code = st.text_input("City Postal Code")
    startup_industry = st.text_input("Company Industry")


    if st.button("Signup"):
        st.success("You have successfully created a Profile")
  

def reading_data():
    df= pd.read_csv('AIStartupLandscape-DK.csv', index_col=0)
    return df

signup_form()
