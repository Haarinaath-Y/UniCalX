from converters.unitconverter import UnitConverter


# Factory function for creating converters
def get_converter(unit_type):
    return UnitConverter(unit_type)