import streamlit as st


class ConverterUI:
    def __init__(self, converter, title, instance_id=1):
        self.converter = converter
        self.title = title
        self.instance_id = instance_id

    def display(self):
        st.subheader(f"{self.title} Conversion")

        col1, col2 = st.columns(2)

        # User inputs
        with col1:
            from_unit = st.selectbox("From unit:", [unit.title() for unit in self.converter.units.keys()], key=f"{self.title}_from_unit_{self.instance_id}")
            to_unit = st.selectbox("To unit:", [unit.title() for unit in self.converter.units.keys()], key=f"{self.title}_to_unit_{self.instance_id}")

        with col2:
            value = st.number_input("Enter value:", value=1.0, step=0.01, key=f"{self.title}_value_unit_{self.instance_id}")

            # Convert back to lowercase for internal processing
            from_unit_key = from_unit.lower()
            to_unit_key = to_unit.lower()

            if from_unit == to_unit:
                st.markdown("**Result:**")
                st.markdown(f"{value:.4f}")
            else:
                result = self.converter.convert(value, from_unit_key, to_unit_key)
                if isinstance(result, str):
                    st.error(result)
                else:
                    st.markdown("**Result:**")
                    st.markdown(f"{result:.4f}")
