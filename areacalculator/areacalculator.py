from math import pi
from converters.unitconverter import UnitConverter


class AreaCalculator:
    def __init__(self, unit_converter: UnitConverter):
        self.unit_converter = unit_converter

    def calculate_rectangle_area(self, length, width, from_unit, to_unit):
        area = length * width
        return area, self.unit_converter.convert(area, from_unit, to_unit)

    def calculate_circle_area(self, radius, from_unit, to_unit):
        area = pi * (radius ** 2)
        return area, self.unit_converter.convert(area, from_unit, to_unit)

    def calculate_triangle_area(self, base, height, from_unit, to_unit):
        area = 0.5 * base * height
        return area, self.unit_converter.convert(area, from_unit, to_unit)




