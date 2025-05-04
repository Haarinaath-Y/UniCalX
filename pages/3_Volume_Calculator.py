from areacalculator.areacalculator import AreaCalculator
from volumecalculator.volumecalculator import VolumeCalculator
from volumecalculator.volumecalculatorui import VolumeCalculatorUI
import streamlit as st
from utils import get_converter


st.set_page_config(
    page_title='Volume Calculator',
    layout="wide"
)


def volume_calculator():

    # Instantiate the volumeCalculator with the "volume" UnitConverter
    shape_volume_calculator = VolumeCalculator(get_converter("volume"))
    volume_calculator_ui = VolumeCalculatorUI(
        shape_volume_calculator,
        "Volume",
        instance_id=1,
        from_unit=shape_volume_calculator.unit_converter.default_from,
        to_unit=shape_volume_calculator.unit_converter.default_to
    )
    volume_calculator_ui.display_volume_calculator()


if __name__ == "__main__":
    volume_calculator()
    