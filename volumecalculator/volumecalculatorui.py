import streamlit as st

class VolumeCalculatorUI:
    def __init__(self, volume_calculator, title, instance_id=1, from_unit=None, to_unit=None):
        self.volume_calculator = volume_calculator
        self.title = title
        self.instance_id = instance_id
        self.from_unit = from_unit
        self.to_unit = to_unit


    def display_volume_calculator(self):
        st.header(f"{self.title} Calculator")

        # Define shape-specific input fields and calculation methods
        shapes = {
            "Cube": {
                "inputs": [("Enter side length:", 1.0)],
                "method": self.volume_calculator.calculate_cube_volume
            },
            "Cuboid": {
                "inputs": [("Enter length:", 1.0), ("Enter width:", 1.0), ("Enter height:", 1.0)],
                "method": self.volume_calculator.calculate_cuboid_volume
            },
            "Cylinder": {
                "inputs": [("Enter radius:", 1.0), ("Enter height:", 1.0)],
                "method": self.volume_calculator.calculate_cylinder_volume
            },
            "Sphere": {
                "inputs": [("Enter radius:", 1.0)],
                "method": self.volume_calculator.calculate_sphere_volume
            }
        }

        # Select shape
        shape = st.selectbox("Select a shape:", list(shapes.keys()))

        # Input dimensions dynamically
        inputs = []
        for label, default in shapes[shape]["inputs"]:
            inputs.append(st.number_input(label, value=default, step=0.01))

        # Select units
        from_unit = st.selectbox("From unit:", [unit.capitalize() for unit in self.volume_calculator.unit_converter.units.keys()])
        to_unit = st.selectbox("To unit:", [unit.capitalize() for unit in self.volume_calculator.unit_converter.units.keys()])

        # Calculate volume
        volume_result, converted_result = shapes[shape]["method"](*inputs, from_unit.lower(), to_unit.lower())

        # Display result
        if isinstance(volume_result, str):
            st.error(volume_result)
        else:
            st.success(f"{self.title} of {shape}: {volume_result:.4f} {from_unit} = {converted_result:.4f} {to_unit}")
