import streamlit as st
from converters.converterui import ConverterUI
from converters.unitconverter import UnitConverter


st.set_page_config(page_title="UniCalX", page_icon="💻", layout="wide")
st.title("💻 UniCalX")
st.sidebar.success("Navigate yourself")


# Factory function for creating converters
def get_converter(unit_type):
    return UnitConverter(unit_type)


# Instantiate the converter outside the Streamlit app flow for efficiency
conversion_options = {
    "Length": lambda: get_converter("length"),
    "Weight": lambda: get_converter("weight"),
    "Volume": lambda: get_converter("volume"),
    "Area": lambda: get_converter("area"),
    "Speed": lambda: get_converter("speed"),
    "Force": lambda: get_converter("force"),
    "Temperature": lambda: get_converter("temperature"),
}

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

