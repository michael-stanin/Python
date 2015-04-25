from user import User


class Student(User):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def gender(self):
        return self.gender_

    @gender.setter
    def gender(self, value):
        if value in ("male", "female"):
            self.gender_ = value
        else:
            self.gender_ = None
