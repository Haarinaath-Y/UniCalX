import streamlit as st

class BMICalculator:
    @staticmethod
    def calculate_bmi(weight, height):
        if height > 0:
            return weight / (height ** 2)
        return None

    @staticmethod
    def get_bmi_category(bmi):
        if bmi is None:
            return "Invalid BMI"
        elif bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

    @staticmethod
    def get_bmi_category_text(bmi, category):
        if bmi is not None:
            st.success(f"Your BMI is: {bmi:.2f}")
            if category == "Underweight":
                st.warning("You are underweight. Consider consulting a healthcare provider for advice.")
            elif category == "Normal weight":
                st.success("You have a normal weight. Keep up the good work!")
            elif category == "Overweight":
                st.warning("You are overweight. Consider a balanced diet and regular exercise.")
            elif category == "Obesity":
                st.error("You are in the obesity range. It's important to consult a healthcare provider.")
        else:
            st.error("Please enter valid weight and height values.")