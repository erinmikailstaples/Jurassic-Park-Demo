import streamlit as st
import pandas as pd
import plost
import altair as alt

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

st.title('Jurassic Park Control Room')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

## Sidebar

st.sidebar.header('Control Panel')

st.sidebar.markdown('''
---
Created with ❤️ by [Erin Mikail Staples](https://erinmikailstaples.com).
                    
Based off of the [Streamlit App Starter Kit](https://github.com/streamlit/app-starter-kit) by [Data Professor](https://www.youtube.com/channel/UCV8e2g4IWQqK71bbzGDEI4Q).
''')

## Main Page Content

# Row A
st.markdown('## Recent Events')
col1, col2, col3 = st.columns(3)
col1.metric("Recent Incidents", "13", "1")
col2.metric("Number of Dinosaurs", "29", "-2")
col3.metric("Guests In Park", "112", "-11%")

# Row B
dino_data = pd.read_csv('https://raw.githubusercontent.com/erinmikailstaples/Jurassic-Park-Demo/main/dinosaur-data.csv', usecols=['name', 'period', 'diet', 'weight', 'height', 'length', 'speed', 'era', 'continent', 'description'])



st.markdown('### All Dinosaurs')
    
st.bar_chart(dino_data['period'], height=345, use_container_width=True)

