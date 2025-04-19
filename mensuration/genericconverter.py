from converters.unitconverter import UnitConverter


class GenericConverter(UnitConverter):
    def __init__(self, unit_type):
        super().__init__(unit_type)
