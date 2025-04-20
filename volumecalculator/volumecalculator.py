from math import pi
from converters.unitconverter import UnitConverter


class VolumeCalculator:
    def __init__(self, unit_converter: UnitConverter):
        self.unit_converter = unit_converter

    def calculate_cube_volume(self, side, from_unit, to_unit):
        volume = side ** 3
        converted_volume = self.unit_converter.convert(volume, from_unit, to_unit)
        return volume, converted_volume

    def calculate_cuboid_volume(self, length, width, height, from_unit, to_unit):
        volume = length * width * height
        converted_volume = self.unit_converter.convert(volume, from_unit, to_unit)
        return volume, converted_volume

    def calculate_cylinder_volume(self, radius, height, from_unit, to_unit):
        volume = radius * height
        converted_volume = self.unit_converter.convert(volume, from_unit, to_unit)
        return volume, converted_volume

    def calculate_sphere_volume(self, radius, from_unit, to_unit):
        volume = (4 / 3) * pi * (radius ** 3)
        converted_volume = self.unit_converter.convert(volume, from_unit, to_unit)
        return volume, converted_volume

