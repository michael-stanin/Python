

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
            raise ValueError("First name for user is empty!")

    @property
    def last_name(self):
        return self.last_name_

    @last_name.setter
    def last_name(self, value):
        if value != "":
            self.last_name_ = value
        else:
            raise ValueError("Last name for user is empty!")

    @property
    def rights(self):
        return self.rights_

    @rights.setter
    def rights(self, value):
        if value in ("administrator", "student"):
            self.rights_ = value
        else:
            raise ValueError(
                "{} is not possible value for rights".format(value))
