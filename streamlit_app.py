import streamlit as st
import pandas as pd
import plost

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

st.title('Jurassic Park Control Room')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('current status')

st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max')) 

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('q2', 'q3'))

st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

st.sidebar.markdown('''
---
Created with ❤️ by [Erin Mikail Staples](https://erinmikailstaples.com).
Based off of the [Streamlit App Starter Kit](https://github.com/streamlit/app-starter-kit) by [Data Professor](https://www.youtube.com/channel/UCV8e2g4IWQqK71bbzGDEI4Q).
''')


# Row A
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

# Row B
dino_data = pd.read_csv('https://raw.githubusercontent.com/erinmikailstaples/Jurassic-Park-Demo/main/dinosaur-data.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/erinmikailstaples/Jurassic-Park-Demo/main/dinosaur-data.csv')

c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap')
    plost.time_hist(
    data=dino_data,
    date='date',
    x_unit='week',
    y_unit='day',
    color=time_hist_color,
    aggregate='median',
    legend=None,
    height=345,
    use_container_width=True)
with c2:
    st.markdown('### Donut chart')
    plost.donut_chart(
        data=dino_data,
        theta=donut_theta,
        color='company',
        legend='bottom', 
        use_container_width=True)

# Row C
st.markdown('### Line chart')
st.line_chart(dino_data, x = 'date', y = plot_data, height = plot_height)