import streamlit as st
import re
import pandas as pd

st.set_page_config(
    page_title='Phone Number Formatter',
    page_icon=':telephone_receiver:',
    layout='wide')

hide_streamlit_style = '''
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            '''            
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

@st.cache_data
def get_data():
    data = pd.read_csv('Databases/Country Codes.csv')
    return data

data = get_data().copy()

st.title('Phone Number Formatter')

phone_number = st.text_input('Enter the phone number')

phone_number = re.sub('[^0-9]', '', phone_number)
st.write('<br>', unsafe_allow_html=True)

st.write('Formatted phone number:')

st.code(phone_number)

st.divider()

st.header('Country codes')

st.dataframe(data, hide_index=True, use_container_width=True)
