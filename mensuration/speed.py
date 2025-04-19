from converters.unitconverter import UnitConverter


class SpeedConverter(UnitConverter):
    """
    Handles speed unit conversions.
    Base unit: meters per second (m/s)
    """
    def __init__(self):
        super().__init__("speed")
