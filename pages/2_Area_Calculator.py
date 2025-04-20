from areacalculator.areacalculator import AreaCalculator
from areacalculator.areacalculatorui import AreaCalculatorUI
import streamlit as st
from utils import get_converter


st.set_page_config(
    page_title='Area Calculator',
    layout="wide"
)


def area_calculator():

    # Instantiate the AreaCalculator with the "area" UnitConverter
    shape_area_calculator = AreaCalculator(get_converter("area"))
    area_calculator_ui = AreaCalculatorUI(
        shape_area_calculator.unit_converter,
        "Area",
        instance_id=1,
        from_unit=shape_area_calculator.unit_converter.default_from,
        to_unit=shape_area_calculator.unit_converter.default_to
    )
    area_calculator_ui.display_area_calculator()


if __name__ == "__main__":
    area_calculator()
    