from converters.unitconverter import UnitConverter


class TemperatureConverter(UnitConverter):
    def __init__(self, unit_type="temperature"):
        super().__init__(unit_type)

    def convert_to_base(self, value, from_unit):
        # Convert temperature to Kelvin (base unit)
        if from_unit == "celsius":
            return value + 273.15
        elif from_unit == "fahrenheit":
            return (value - 32) * 5 / 9 + 273.15
        elif from_unit == "kelvin":
            return value
        else:
            return "Invalid 'from' unit for temperature"

    def convert_from_base(self, base_value, to_unit):
        # Convert temperature from Kelvin to the target unit
        if to_unit == "celsius":
            return base_value - 273.15
        elif to_unit == "fahrenheit":
            return (base_value - 273.15) * 9 / 5 + 32
        elif to_unit == "kelvin":
            return base_value
        else:
            return "Invalid 'to' unit for temperature"
