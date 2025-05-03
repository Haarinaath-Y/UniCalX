import streamlit as st
from converters.converterui import ConverterUI
from converters.converter_registry import ConverterRegistry
from utils import get_headers

st.set_page_config(page_title="UniCalX", page_icon="💻", layout="wide")
st.title("💻 UniCalX")
st.sidebar.success("🌟 Navigate yourself")

st.info("""
### Welcome to UniCalX! 💻

UniCalX is a versatile unit conversion tool designed to make your calculations quick and easy. Here's how you can use this app:

1. **Default Conversions**: The app provides quick access to commonly used conversions like Length, Area, and Volume. Simply input your values and get instant results.

2. **Custom Conversions**: Use the dropdown menu to select additional conversion types, such as Temperature or other units available in the app.

3. **Interactive Interface**: Adjust the input values, select units, and view the results in real-time.

Whether you're a student, engineer, or just need quick conversions, UniCalX has you covered!

Enjoy seamless and accurate unit conversions!
""")

# Use the cached function to get headers
headers = get_headers()


# Define default conversion types
st.header("🚀 Quick Conversions")
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
st.header("Other Conversion Types")
conversion_type1 = st.selectbox("Select conversion type:", headers)
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
