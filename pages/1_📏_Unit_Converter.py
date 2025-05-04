import streamlit as st
from utils import get_cached_converter, display_converter

def unit_converter():
    # Define default conversion types
    st.header("🚀 Quick Conversions")
    default_conversions = ["Length", "Area", "Volume"]
    for conversion_type in default_conversions:
        converter = get_cached_converter(conversion_type)
        display_converter(conversion_type)
        st.divider()

    # Allow user to select additional conversion types
    st.header("Other Conversion Types")
    conversion_type1 = st.selectbox("Select conversion type:", ["Speed", "Weight", "Temperature", "Force", "Energy", "Power", "Time", "Data", "Length", "Area", "Volume"])
    if conversion_type1:
        converter = get_cached_converter(conversion_type1)
        display_converter(conversion_type1, instance_id=2)

if __name__ == "__main__":
    unit_converter()
