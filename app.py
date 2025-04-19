import streamlit as st
from typing import Callable, Dict
from converters.converterui import ConverterUI
from converters.unitconverter import UnitConverter
from mensuration.temperature import TemperatureConverter


st.set_page_config(page_title="UniCalX", page_icon="💻", layout="wide")
st.title("💻 UniCalX")
st.sidebar.success("Navigate yourself")


# Factory function for creating converters
def get_converter(unit_type):
    return UnitConverter(unit_type)


# Instantiate the converter outside the Streamlit app flow for efficiency

# Define the type for conversion options
ConversionOptionsType = Dict[str, Callable[[], UnitConverter]]

unit_types = ["length", "weight", "volume", "area", "speed", "force"]

# Dynamically generate conversion options
conversion_options: ConversionOptionsType = {
    unit_type.capitalize(): lambda u=unit_type: get_converter(u) for unit_type in unit_types
}
# Add TemperatureConverter separately
conversion_options["Temperature"] = lambda: TemperatureConverter()

# Display default conversion types
default_conversions = ["Length", "Area", "Volume"]
for i, conversion_type in enumerate(default_conversions):
    converter = conversion_options[conversion_type]()
    ui = ConverterUI(converter, conversion_type)
    ui.display()

# Allow user to select additional conversion types
conversion_type1 = st.selectbox("Select conversion type:", list(conversion_options.keys()), key='selection1')
if conversion_type1:
    converter = conversion_options[conversion_type1]()
    ui = ConverterUI(converter, conversion_type1, instance_id=2)
    ui.display()

