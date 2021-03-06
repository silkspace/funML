import streamlit as st
import requests
import csv
from datetime import datetime


st.header('Unblock and Be Inspired')
size = st.selectbox(
    'How long a response do you want?',
    ('Tweet', 'Paragraph', 'Page')
)

lmaps = {'Tweet': 120, 'Paragraph': 320, 'Page': 1000}

context = st.text_area('Write your best opening paragraph here:', 'A Quantum theory of Gravity needs at least three unique attributes;')

@st.cache
def generate_text(context):
    payload = {
        "context": context,
        "token_max_length": lmaps[size],
        "temperature": 1.0,
        "top_p": 0.9,
    }
    response = requests.post("http://api.vicgalle.net:5000/generate", params=payload).json()
    return response

response = generate_text(context)

#st.subheader('Here we go!')
st.caption(context)
st.write(response['text'])

full_text = context + '  ' + response['text']

st.download_button('Download your Custom Response', full_text)
#st.balloons()

st.header('')
st.write("check out [TensorML](https://www.tensorml.com) for more")

@st.cache
def save_response():
    writer = csv.writer(open('./generated.csv', 'a'))
    writer.writerow([size, context, response['text'], datetime.now()])
    print('saved')
    
save_response()
