from converters.unitconverter import UnitConverter


class ForceConverter(UnitConverter):
    """
    Handles force unit conversions.
    Base unit: Newton (N)
    """
    def __init__(self):
        super().__init__("force")