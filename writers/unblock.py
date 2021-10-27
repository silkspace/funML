import streamlit as st
import requests

size = st.sidebar.selectbox(
    'How long a response do you want?',
    ('Tweet Length', 'Paragraph', 'Page')
)

st.write(size)

lmaps = {'Tweet Length': 120, 'Paragraph': 320, 'Page': 1000}

context = st.text_area('Write your best opening paragraph here', 'A Quantum theory of Gravity needs at least three unique attributes;')

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

st.subheader('')
st.download_button('Download your Custom Response', response['text'])
#st.balloons()