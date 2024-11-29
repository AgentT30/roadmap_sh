import streamlit as st

st.title("Unit Converter")

if st.button("Home"):
    st.switch_page("app.py")
if st.button("Length"):
    st.switch_page("pages/length.py")
if st.button("Weight"):
    st.switch_page("pages/weight.py")
if st.button("Temperature"):
    st.switch_page("pages/temperature.py")