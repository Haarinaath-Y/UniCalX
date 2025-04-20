import streamlit as st


class AreaCalculatorUI:
    def __init__(self, area_calculator, title, instance_id=1, from_unit=None, to_unit=None):
        self.area_calculator = area_calculator
        self.title = title
        self.instance_id = instance_id
        self.from_unit = from_unit
        self.to_unit = to_unit

    def display_area_calculator(self):
        st.header(f"{self.title} Calculator")

        # Define shape-specific input fields and calculation methods
        shapes = {
            "Rectangle": {
                "inputs": [("Enter length:", 1.0), ("Enter width:", 1.0)],
                "method": self.area_calculator.calculate_rectangle_area
            },
            "Circle": {
                "inputs": [("Enter radius:", 1.0)],
                "method": self.area_calculator.calculate_circle_area
            },
            "Triangle": {
                "inputs": [("Enter base:", 1.0), ("Enter height:", 1.0)],
                "method": self.area_calculator.calculate_triangle_area
            }
        }

        # Select shape
        shape = st.selectbox("Select a shape:", list(shapes.keys()))

        # Input dimensions dynamically
        inputs = []
        for label, default in shapes[shape]["inputs"]:
            inputs.append(st.number_input(label, value=default, step=0.01))

        # Select units
        from_unit = st.selectbox("From unit:", [unit.title() for unit in self.area_calculator.unit_converter.units.keys()])
        to_unit = st.selectbox("To unit:", [unit.title() for unit in self.area_calculator.unit_converter.units.keys()])

        # Calculate area
        input_unit_result, output_unit_result = shapes[shape]["method"](*inputs, from_unit.lower(), to_unit.lower())

        # Display result
        if isinstance(input_unit_result, str):
            st.error(input_unit_result)
        else:
            st.success(f"{self.title} of {shape}: {input_unit_result:.4f} {from_unit} = {output_unit_result:.4f} {to_unit}")