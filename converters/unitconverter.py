import yaml


class UnitConverter:
    def __init__(self, unit_type):
        self.units = self.load_units(unit_type)

    @staticmethod
    def load_units(unit_type):
        try:
            with open("units.yaml", "r") as file:
                data = yaml.safe_load(file)
                if unit_type not in data:
                    raise ValueError(f"Unit type '{unit_type}' not found in configuration.")
                return data[unit_type]
        except FileNotFoundError:
            raise FileNotFoundError("The units.yaml configuration file is missing.")
        except yaml.YAMLError:
            raise ValueError("The units.yaml file contains invalid YAML.")

    def convert_to_base(self, value, from_unit):
        if from_unit not in self.units:
            return "Invalid 'from' unit"
        return float(value) * float(self.units[from_unit])

    def convert_from_base(self, base_value, to_unit):
        if to_unit not in self.units:
            return "Invalid 'to' unit"
        return float(base_value) / float(self.units[to_unit])

    def convert(self, value, from_unit, to_unit):
        base_value = self.convert_to_base(value, from_unit)
        if isinstance(base_value, str):
            return base_value
        result = self.convert_from_base(base_value, to_unit)
        return result
