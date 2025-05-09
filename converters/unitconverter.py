import yaml
import streamlit as st


class UnitConverter:
    _unit_data_cache = {}

    """A base class for unit conversion."""
    def __init__(self, unit_type):
        self.unit_type = unit_type
        self.data = self.load_units(unit_type)
        self.units = self.data.get("units", {})
        self.default_from = self.data.get("default_from")
        self.default_to = self.data.get("default_to")

    @staticmethod
    def load_units(unit_type):
        if not UnitConverter._unit_data_cache:
            try:
                with open("units.yaml", "r") as file:
                    UnitConverter._unit_data_cache = yaml.safe_load(file)
            except FileNotFoundError:
                raise FileNotFoundError("The units.yaml configuration file is missing.")
            except yaml.YAMLError:
                raise ValueError("The units.yaml file contains invalid YAML.")

        if unit_type not in UnitConverter._unit_data_cache:
            raise ValueError(f"Unit type '{unit_type}' not found in configuration.")
        return UnitConverter._unit_data_cache[unit_type]

    def convert_to_base(self, value, from_unit):
        if from_unit not in self.units:
            return f"Error: '{from_unit}' is not a valid unit for {self.unit_type}."
        return float(value) * float(self.units[from_unit])

    def convert_from_base(self, base_value, to_unit):
        if to_unit not in self.units:
            return f"Error: '{to_unit}' is not a valid unit for {self.unit_type}."
        return float(base_value) / float(self.units[to_unit])

    def convert(self, value, from_unit, to_unit):
        # Validate the input value
        if self.unit_type != "temperature" and (not isinstance(value, (int, float)) or value <= 0):
            st.error(f"Invalid input: {value}. Value must be a positive number for {self.unit_type}.")
            return None

        # Convert to base unit
        base_value = self.convert_to_base(value, from_unit)
        if isinstance(base_value, str):  # Check for error message
            st.error("Kindly check the input value.")
            return None

        # Convert from base unit to target unit
        result = self.convert_from_base(base_value, to_unit)
        if isinstance(result, str):  # Check for error message
            st.error("Kindly check the input value.")
            return None

        return result
