from converters.unitconverter import UnitConverter
from converters.converter_registry import ConverterRegistry
from converters.converterui import ConverterUI
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

# Cache the converters to avoid repeated lookups
@st.cache_resource
def get_cached_converter(conversion_type):
    return ConverterRegistry.get_converter(conversion_type.lower())

# Reusable function to display a converter
def display_converter(conversion_type, instance_id=None):
    converter = get_cached_converter(conversion_type)
    ui = ConverterUI(
        converter,
        conversion_type,
        instance_id=instance_id,
        from_unit=converter.default_from,
        to_unit=converter.default_to
    )
    ui.display()
