import streamlit as st


class ConverterUI:
    def __init__(self, converter, title):
        self.converter = converter
        self.title = title

    def display(self):
        st.subheader(f"{self.title} Conversion")

        col1, col2 = st.columns(2)

        # User inputs
        with col1:
            from_unit = st.selectbox("From unit:", list(self.converter.units.keys()))
            to_unit = st.selectbox("To unit:", list(self.converter.units.keys()))

        with col2:
            value = st.number_input("Enter value:", value=1.0, step=0.01)

            if from_unit == to_unit:
                st.write(f"{value:.2f}")
                st.warning("Please select different units for conversion.")
            else:
                result = self.converter.convert(value, from_unit, to_unit)
                if isinstance(result, str):
                    st.error(result)
                else:
                    st.write(f"{result:.4f}")

