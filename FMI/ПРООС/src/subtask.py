

class Subtask:

    def __init__(self, *args, **kwargs):
        pass

    @property
    def title(self):
        return self.title_

    @title.setter
    def title(self, value):
        if value != "":
            self.title_ = value
        else :
            raise ValueError("Title for Subtask is empty!")

    @property
    def content(self):
        return self.content_

    @content.setter
    def content(self, value):
        if value != "":
            self.content_ = value
        else:
            raise ValueError("Content for Subtask is empty!")

    @property
    def state(self):
        return self.state_

    @state.setter
    def state(self, value):
        # None will be used when the student hasn't started a subtask yet
        # Started will be used when the student is working on the subtask
        # Finished will be used when the student is done with the subtask
        if value in ("None", "Started", "Finished"):
            self.state_ = value
        else:
            raise ValueError("{} is not a correct State!")
