import streamlit as st
from areacalculator.areacalculator import AreaCalculator


class AreaCalculatorUI:
    def __init__(self, converter, title, instance_id=1, from_unit=None, to_unit=None):
        self.converter = converter
        self.title = title
        self.instance_id = instance_id
        self.from_unit = from_unit
        self.to_unit = to_unit
        self.shape_calculator = AreaCalculator(converter)

    def display_area_calculator(self):
        st.header(f"{self.title} Calculator")

        # Define shape-specific input fields and calculation methods
        shapes = {
            "Rectangle": {
                "inputs": [("Enter length:", 1.0), ("Enter width:", 1.0)],
                "method": self.shape_calculator.calculate_rectangle_area
            },
            "Circle": {
                "inputs": [("Enter radius:", 1.0)],
                "method": self.shape_calculator.calculate_circle_area
            },
            "Triangle": {
                "inputs": [("Enter base:", 1.0), ("Enter height:", 1.0)],
                "method": self.shape_calculator.calculate_triangle_area
            }
        }

        # Select shape
        shape = st.selectbox("Select a shape:", list(shapes.keys()))

        # Input dimensions dynamically
        inputs = []
        for label, default in shapes[shape]["inputs"]:
            inputs.append(st.number_input(label, value=default, step=0.01))

        # Select units
        from_unit = st.selectbox("From unit:", list(self.converter.units.keys()))
        to_unit = st.selectbox("To unit:", list(self.converter.units.keys()))

        # Calculate area
        result = shapes[shape]["method"](*inputs, from_unit, to_unit)

        # Display result
        if isinstance(result, str):
            st.error(result)
        else:
            st.success(f"Area: {result:.4f} {to_unit}")