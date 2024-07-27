import streamlit as st

st.set_page_config(
    page_title="Homepage",
    page_icon="👋",
)

st.title('My First Streamlit App')

st.write('Navigate to other pages:')

st.link_button('Text Page', url='Text_Page')
st.link_button('📺 Media Page', url='Media_Page')