import streamlit as st

st.title("Length Converter")

input_length = st.text_input("Enter Length to Convert")

from_unit = st.selectbox("Unit to convert from", ("millimeters", "centimeters", "meters", "kilometer", "inch", "foot", "yard", "mile"))
to_unit = st.selectbox("Unit to convert to", ("millimeters", "centimeters", "meters", "kilometer", "inch", "foot", "yard", "mile"))

if st.button("Submit"):
    try:
        input_length = float(input_length)
    except:
        st.error("Given input must be numeric!")

    factors = {"millimeters": 0.001, "centimeters": 0.01, "meters": 1.0, "kilometer": 1000.0, "inch": 0.0254, "foot": 0.3048, "yard": 0.917, "mile": 1609}
    st.success(f"{round(input_length * factors[from_unit]/factors[to_unit], 2)} {to_unit}")