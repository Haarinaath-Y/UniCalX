from converters.unitconverter import UnitConverter


class VolumeConverter(UnitConverter):
    """
    Handles volume unit conversions.
    Base unit: cubic meters (m^3)
    """
    def __init__(self):
        super().__init__("volume")