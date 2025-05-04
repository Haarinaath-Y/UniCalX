import streamlit as st
from bmicalculator.bmicalculator import BMICalculator

title = "️‍️‍️‍🏋️‍♂️ BMI Calculator"
st.set_page_config(
    page_title=title,
    layout="wide"
)

def bmi_calculator():
    st.title(title)

    st.info("""
    ### Calculate Your BMI
    Enter your weight and height to calculate your Body Mass Index (BMI) and determine your BMI category.
    """)

    # Input fields for weight and height
    weight = st.number_input("Enter your weight (in kilograms):", min_value=0.0, step=0.1, format="%.1f")
    height = st.number_input("Enter your height (in meters):", min_value=0.0, step=0.01, format="%.2f")

    if st.button("Calculate BMI"):
        bmi = BMICalculator.calculate_bmi(weight, height)
        category = BMICalculator.get_bmi_category(bmi)
        BMICalculator.get_bmi_category_text(bmi, category)

if __name__ == "__main__":
    bmi_calculator()