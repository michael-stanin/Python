

class User:

    def __init__(self, *args, **kwargs):
        pass

    @property
    def first_name(self):
        return self.first_name_

    @first_name.setter
    def first_name(self, value):
        self.first_name_ = value

    @property
    def last_name(self):
        return self.last_name_

    @last_name.setter
    def last_name(self, value):
        self.last_name_ = value
