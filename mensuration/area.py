from converters.unitconverter import UnitConverter


class AreaConverter(UnitConverter):
    """
    Handles area unit conversions.
    Base unit: square meters (m^2)
    """
    def __init__(self):
        super().__init__("area")