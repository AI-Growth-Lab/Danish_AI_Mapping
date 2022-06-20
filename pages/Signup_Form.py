#Import libraries
import folium
import branca
import pandas as pd
import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from folium.plugins import Draw
from streamlit_folium import st_folium
import pygsheets
import pandas as pd

def intro():
    st.write("# Welcome to Danish AI Mapping! 👋")

    st.markdown(
        """
Danish AI Mapping is an app built specifically for landscaping AI companies in Denmark.

        """
    )

st.write("# Welcome to Danish AI Mapping!")

st.markdown(
    """
Danish AI Mapping is an app built specifically for landscaping AI companies in Denmark.

    """
)

def singup():
    df_template = pd.DataFrame()
    st.subheader("Create New Profile for Your Company")
    df_template['startup_name'] = [st.text_input("Company Name")]
    df_template['startup_url'] = [st.text_input("Company URL")]
    df_template['startup_founding_year'] = [st.text_input("Company Founding Year")]
    df_template['city_state'] = [st.text_input("City")]
    df_template['address_street'] = [st.text_input("Street")]
    df_template['address_code'] = [st.text_input("City Postal Code")]
    df_template['startup_industry'] = [st.text_input("Company Industry")]
    

    if st.button("Signup"):
        st.success("You have successfully created a Profile")
        #authorization
        SAMPLE_SPREADSHEET_ID = '1jzoF2XLAGtY2yGgjp0mPSlta6KSVg6omHO8ScOOaRSU'
        gc = pygsheets.authorize(service_file='https://github.com/HamidBekamiri/Danish_AI_Mapping/blob/main/pages/keys.json')
        sht1 = gc.open_by_key(SAMPLE_SPREADSHEET_ID)
        #select the first sheet 
        wks = sht1[0]
        # df_c = wks.get_as_df(has_header=True)
        # s = pd.Series(df_c['startup_name'].to_list())
        # st.write(df_c)
        # b = df_template['startup_name']
        # st.write(type(b))
        # st.write(b)
        # st.write(type(s))
        # st.write(s)

        # if b in s:
        #     return st.success("This profile has already been created!")
        # else:     
        values = df_template.values.tolist()
        return wks.append_table(values, start='A1', end=None, dimension='ROWS', overwrite=False)
       

def reading_data():
    df= pd.read_csv('AIStartupLandscape-DK.csv', index_col=0)
    return df

singup()

