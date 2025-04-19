from converters.unitconverter import UnitConverter


class TemperatureConverter(UnitConverter):
    """
    Handles temperature unit conversions.
    Base unit: Kelvin (K)  (Even though we don't convert *to* Kelvin)
    """

    def __init__(self):
        super().__init__("temperature")

    def convert_to_base(self, value, from_unit):
        """Convert to Kelvin"""
        if from_unit == "Celsius":
            return value + 273.15
        elif from_unit == "Fahrenheit":
            return (value - 32) * 5 / 9 + 273.15
        elif from_unit == "Rankine":
            return value * 5 / 9
        elif from_unit == "Kelvin":
            return value
        else:
            return "Invalid 'from' unit"

    def convert_from_base(self, base_value, to_unit):
        """Convert from Kelvin"""
        if to_unit == "Celsius":
            return base_value - 273.15
        elif to_unit == "Fahrenheit":
            return (base_value - 273.15) * 9 / 5 + 32
        elif to_unit == "Rankine":
            return base_value * 9 / 5
        elif to_unit == "Kelvin":
            return base_value
        else:
            return "Invalid 'to' unit"
