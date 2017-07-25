from filereader import FileReader


UNITS = "units.txt"


class UnitParser:

    def __init__(self):
        self.units_ = FileReader.read_units(UNITS)

    def parse(self):
        unit_names = [name for name in self.units_[::3] if name]
        unit_contents = [content for content in self.units_[1::3] if content]
        print("Names: ", unit_names)
        print("Names: ", unit_contents)
        self.units_ = dict(zip(unit_names, unit_contents))

    def units(self):
        return self.units_
