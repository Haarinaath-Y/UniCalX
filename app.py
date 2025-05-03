import streamlit as st
from converters.converterui import ConverterUI
from converters.converter_registry import ConverterRegistry


st.set_page_config(page_title="UniCalX", page_icon="💻", layout="wide")
st.title("💻 UniCalX")
st.sidebar.success("Navigate yourself")

# Define default conversion types
default_conversions = ["Length", "Area", "Volume"]
for conversion_type in default_conversions:
    converter = ConverterRegistry.get_converter(conversion_type.lower())
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
conversion_type1 = st.selectbox("Select conversion type:", ["Length", "Area", "Volume", "Temperature", "Force", "Weight", "Speed"])
if conversion_type1:
    converter = ConverterRegistry.get_converter(conversion_type1.lower())
    ui = ConverterUI(
        converter,
        conversion_type1,
        instance_id=2,
        from_unit=converter.default_from,
        to_unit=converter.default_to
    )
    ui.display()
