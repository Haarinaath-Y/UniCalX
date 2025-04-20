import streamlit as st


class ConverterUI:
    def __init__(self, converter, title, instance_id=1, from_unit=None, to_unit=None):
        self.converter = converter
        self.title = title
        self.instance_id = instance_id
        self.from_unit = from_unit
        self.to_unit = to_unit

    @staticmethod
    def create_dropdown(label, options, default, key):
        return st.selectbox(
            label,
            [option.title() for option in options],
            index=options.index(default) if default else 0,
            key=key
        )

    def display(self):
        st.subheader(f"{self.title} Conversion")

        col1, col2 = st.columns(2)

        # User inputs
        with col1:
            from_unit = self.create_dropdown(
                "From unit:",
                list(self.converter.units.keys()),
                self.from_unit,
                f"{self.title}_from_unit_{self.instance_id}"
            )
            to_unit = self.create_dropdown(
                "To unit:",
                list(self.converter.units.keys()),
                self.to_unit,
                f"{self.title}_to_unit_{self.instance_id}"
            )

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
                if result is None:  # Check if validation failed
                    return None
                elif isinstance(result, str):
                    st.error(result)
                else:
                    st.markdown("**Result:**")
                    st.markdown(f"{result:.4f} {to_unit}")