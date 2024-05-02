import streamlit as st
import pandas as pd
import plost

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

st.title('Jurassic Park Control Room')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Control Panel')

st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', 'length') 

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('period', 'q3'))

st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

st.sidebar.markdown('''
---
Created with ❤️ by [Erin Mikail Staples](https://erinmikailstaples.com).
Based off of the [Streamlit App Starter Kit](https://github.com/streamlit/app-starter-kit) by [Data Professor](https://www.youtube.com/channel/UCV8e2g4IWQqK71bbzGDEI4Q).
''')


# Row A
st.markdown('## Recent Events')
col1, col2, col3 = st.columns(3)
col1.metric("Recent Incidents", "13", "1")
col2.metric("Number of Dinosaurs", "29", "-2")
col3.metric("Guests In Park", "112", "-11%")

# Row B
dino_data = pd.read_csv('https://raw.githubusercontent.com/erinmikailstaples/Jurassic-Park-Demo/main/dinosaur-data.csv', parse_names=['name'])

c1  = st.columns((7,3))

with c1:
    st.markdown('### All Dinosaurs')
    plost.bar_chart(
    data='dino_data',
    value='period'
    legend=None,
    height=345,
    use_container_width=True)

