

class User:

    def __init__(self, *args, **kwargs):
        pass

    @property
    def first_name(self):
        return self.first_name_

    @first_name.setter
    def first_name(self, value):
        if value != "":
            self.first_name_ = value
        else:
            self.first_name_ = None

    @property
    def last_name(self):
        return self.last_name_

    @last_name.setter
    def last_name(self, value):
        if value != "":
            self.last_name_ = value
        else:
            self.last_name_ = None

    @property
    def rights(self):
        return self.rights_

    @rights.setter
    def rights(self, value):
        if value in ("administrator", "student"):
            self.rights_ = value
        else:
            self.rights_ = None
