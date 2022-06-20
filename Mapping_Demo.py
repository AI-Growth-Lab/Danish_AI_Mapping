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

def popup_html(row):
    data = reading_data()
    i = row
    startup_name=data['Name'].iloc[i] 
    startup_url=data['Website'].iloc[i]
    startup_founding_year = data['Founding Year'].iloc[i] 
    city_state = data['City'].iloc[i] +", "+ data['Country'].iloc[i]                     
    startup_industry = data['Industry'].iloc[i]


    left_col_color = "#19a7bd"
    right_col_color = "#f2f0d3"
    
    html = """<!DOCTYPE html>
<html>

<head>
<h4 style="margin-bottom:10"; width="200px">{}</h4>""".format(startup_name) + """

</head>
    <table style="height: 126px; width: 350px;">
<tbody>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Startup Name</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(startup_name) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Startup Url</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(startup_url) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Startup Founding Year</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(startup_founding_year) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">City and Country</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(city_state) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Startup Industry</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(startup_industry) + """
</tr>
<tr>

</tr>
</tbody>
</table>
</html>
"""
    return html


def reading_data():
    df= pd.read_csv('AIStartupLandscape-DK.csv', index_col=0)
    return df

def mapping_demo():
    
    st.write("# Welcome to Danish AI Mapping!")

    st.markdown(
        """
Danish AI Mapping is an app built specifically for landscaping AI companies in Denmark.

        """
    )

    df = reading_data()
    cities = df['City'].drop_duplicates().append(pd.Series(['all']))
    make_choice = st.sidebar.selectbox('Select City:', cities, index=5)

    if make_choice == 'all':
        # AgGrid(df.head(2),height=100)
        data = df
    else:
        # AgGrid(df[df['City'] == make_choice].head(2),height=100)
        data = df[df['City'] == make_choice]
    
    location = pd.to_numeric(data['Lat'][:5], downcast='float').mean(), pd.to_numeric(data['Lon'][:5], downcast='float').mean() #Specify the center of the map by using the average of latitude and longitude coordinates
    m = folium.Map(location=location,zoom_start=4) #Create a empty folium map object
    Draw(export=True).add_to(m)

    #Color code the markers to show blue markers for public universities and brown colors for private universities
    for i in range(0,len(data)):
        institution_type = data['City'].iloc[i]
        if institution_type == 'Copenhagen':
            color = 'darkblue'
        else:
            color = 'gray'
        
        html = popup_html(i)
        iframe = branca.element.IFrame(html=html,width=510,height=280)
        popup = folium.Popup(folium.Html(html, script=True), max_width=500)
        folium.Marker([data['Lat'].iloc[i],data['Lon'].iloc[i]], popup=popup,icon=folium.Icon(color=color, icon='university', prefix='fa')).add_to(m)    

 
    output = st_folium(m, width = 700, height=500)

mapping_demo()

 







