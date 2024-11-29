import streamlit as st

st.title("Weight Converter")

input_weight = st.text_input("Enter Weight to be Converted")
from_unit = st.selectbox("Unit to convert from", ("milligrams", "grams","kilograms", "ounces", "pounds"))
to_unit = st.selectbox("Unit to convert to", ("milligrams", "grams","kilograms", "ounces", "pounds"))

if st.button("Submit"):
    try:
        input_weight = float(input_weight)
    except:
        st.error("The input weight must be numeric")
    
    factors = {"milligrams": 0.00001, "grams": 0.001, "kilograms": 1.0, "ounces": 0.0283, "pounds": 0.4545}
    
    st.success(f"{round(input_weight * factors[from_unit] / factors[to_unit], 2)} {to_unit}")
