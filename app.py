import streamlit as st
from typing import Callable, Dict
from converters.converterui import ConverterUI
from converters.unitconverter import UnitConverter
from mensuration.temperature import TemperatureConverter
from utils import get_converter


st.set_page_config(page_title="UniCalX", page_icon="💻", layout="wide")
st.title("💻 UniCalX")
st.sidebar.success("Navigate yourself")

# Instantiate the converter outside the Streamlit app flow for efficiency
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
    ui = ConverterUI(
        converter,
        conversion_type,
        from_unit=converter.default_from,
        to_unit=converter.default_to
    )
    ui.display()
    st.divider()

# Allow user to select additional conversion types
st.header("Select Conversion Type")
conversion_type1 = st.selectbox("Select conversion type:", list(conversion_options.keys()), key='selection1')
if conversion_type1:
    converter = conversion_options[conversion_type1]()
    ui = ConverterUI(
        converter,
        conversion_type1,
        instance_id=2,
        from_unit=converter.default_from,
        to_unit=converter.default_to
    )
    ui.display()
