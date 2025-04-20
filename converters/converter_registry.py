from converters.unitconverter import UnitConverter
from mensuration.temperature import TemperatureConverter


class ConverterRegistry:
    """A registry to store and reuse converter instances."""
    _instances = {}

    @staticmethod
    def get_converter(unit_type):
        if unit_type not in ConverterRegistry._instances:
            if unit_type.lower() == "temperature":
                ConverterRegistry._instances[unit_type] = TemperatureConverter()
            else:
                ConverterRegistry._instances[unit_type] = UnitConverter(unit_type)
        return ConverterRegistry._instances[unit_type]
