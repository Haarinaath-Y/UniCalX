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
st.title("Unit Converter")

conversion_options = {
    "Length": lambda: LengthConverter(),
    "Weight": lambda: WeightConverter(),
    "Volume": lambda: VolumeConverter(),
    "Area": lambda: AreaConverter(),
    "Speed": lambda: SpeedConverter(),
    "Force": lambda: ForceConverter(),
    "Temperature": lambda: TemperatureConverter()
}

conversion_type = st.selectbox("Select conversion type:", list(conversion_options.keys()))

if conversion_type:
    converter = conversion_options[conversion_type]()
    ui = ConverterUI(converter, conversion_type)
    ui.display()
