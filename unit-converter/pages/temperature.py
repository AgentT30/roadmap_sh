import streamlit as st


st.title("Temperature Converter")

input_temp = st.text_input("Enter the input temperature")
from_unit = st.selectbox("Unit to convert from", ("celsius", "fahrenheit", "kelvin"))
to_unit = st.selectbox("Unit to convert to", ("celsius", "fahrenheit", "kelvin"))

if st.button("Submit"):
    try:
        input_temp = float(input_temp)
    except:
        st.error("The input temperature must be valid numeric")


    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        output = (input_temp * (9/5)) + 32
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        output = input_temp + 273.15
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        output = (input_temp - 32) * (5/9)
    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        output = (input_temp - 32) * (5/9) + 273.15
    elif from_unit == to_unit:
        output = input_temp
    st.success(f"{output}")