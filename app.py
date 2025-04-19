import streamlit as st
from mensuration.length import LengthConverter
from mensuration.weight import WeightConverter
from mensuration.area import AreaConverter
from mensuration.volume import VolumeConverter
from mensuration.speed import SpeedConverter
from mensuration.force import ForceConverter
from mensuration.temperature import TemperatureConverter
from converters.converterui import ConverterUI

st.set_page_config(page_title="UniCalX", page_icon="💻", layout="wide")
st.title("💻 UniCalX")
st.sidebar.success("Navigate yourself")


# Instantiate the converter outside the Streamlit app flow for efficiency

conversion_options = {
    "Length": lambda: LengthConverter(),
    "Weight": lambda: WeightConverter(),
    "Volume": lambda: VolumeConverter(),
    "Area": lambda: AreaConverter(),
    "Speed": lambda: SpeedConverter(),
    "Force": lambda: ForceConverter(),
    "Temperature": lambda: TemperatureConverter()
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

