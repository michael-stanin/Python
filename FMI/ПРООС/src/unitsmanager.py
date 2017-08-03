from os import path
from filereader import units


class UnitsManager:

    def __init__(self):
        self.units_info = units()
        self.units = self._init_units()
        self.current_unit_idx = 0
        self.current_ex_idx = 0
        self.current_unit_ = self.units[self.current_unit_idx]
        self.current_ex_ = self.current_unit_.exercises[self.current_ex_idx]

    def _init_units(self):
        return [Unit(unit[0], unit[1], unit[2]) for unit in self.units_info]

    @property
    def current_unit(self):
        return self.current_unit_

    @current_unit.setter
    def current_unit(self, value):
        self.current_unit_ = value

    @property
    def current_ex(self):
        return self.current_ex_

    @current_ex.setter
    def current_ex(self, value):
        self.current_ex_ = value

    def next_unit(self):
        if self.current_unit_idx < len(self.units):
            self.current_unit_idx += 1
            self.current_unit = self.units[self.current_unit_idx]
            self.current_ex_idx = 0
            self.current_ex_ = self.current_unit_.exercises[self.current_ex_idx]

    def previous_unit(self):
        if self.current_unit_idx > 0:
            self.current_unit_idx -= 1
            self.current_unit = self.units[self.current_unit_idx]
            self.current_ex_idx = 0
            self.current_ex_ = self.current_unit_.exercises[self.current_ex_idx]

    def next_ex(self):
        if self.current_ex_idx < len(self.current_unit.exercises):
            self.current_ex_idx += 1
            self.current_ex = self.current_unit.exercises[self.current_ex_idx]

    def previous_ex(self):
        if self.current_ex_idx > 0:
            self.current_ex_idx -= 1
            self.current_ex = self.current_unit.exercises[self.current_ex_idx]

    def current_ex_path(self):
        return path.join(self.current_unit.path, "ex" + str(self.current_ex_idx+1))


class Unit:

    def __init__(self, name, path, exercises):
        self.name_ = name
        self.path_ = path
        self.exercises_ = exercises

    @property
    def name(self):
        return self.name_

    @name.setter
    def name(self, value):
        self.name_ = value

    @property
    def path(self):
        return self.path_

    @path.setter
    def path(self, value):
        self.path_ = value

    @property
    def exercises(self):
        return self.exercises_

    @exercises.setter
    def exercises(self, value):
        self.exercises_ = value

    def intro_path(self):
        return path.join(self.path, "intro")

    def dictation_path(self):
        return path.join(self.path, "dictation")
