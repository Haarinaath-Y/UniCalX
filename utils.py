from converters.unitconverter import UnitConverter
import streamlit as st
import yaml


# Factory function for creating converters
def get_converter(unit_type):
    return UnitConverter(unit_type)

@st.cache_data
def get_headers():
    # Load the YAML file using a streaming parser
    with open("units.yaml", "r") as file:
        data = yaml.load(file, Loader=yaml.CSafeLoader)
    # Extract the top-level keys and convert them to capital case
    return [key.capitalize() for key in data.keys()]
