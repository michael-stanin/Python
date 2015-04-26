from subtask import Subtask


class Task:

    def __init__(self, *args, **kwargs):
        self.subtasks_ = []

    @property
    def title(self):
        return self.title_

    @title.setter
    def title(self, value):
        if value != "":
            self.title_ = value
        else :
            raise ValueError("Title for Task is empty!")

    @property
    def content(self):
        return self.content_

    @content.setter
    def content(self, value):
        if value != "":
            self.content_ = value
        else:
            raise ValueError("Content for Task is empty!")

    @property
    def subtasks(self):
        return self.subtasks_

    @subtasks.setter
    def subtasks(self, value):
        if isinstance(value, list) and value:
            self.subtasks_ = value
        else:
            raise ValueError("Subtasks for Task are empty!")

    def add_subtask(self, subtask):
        if isinstance(subtask, Subtask):
            self.subtasks_.append(subtask)
        else:
            raise ValueError("{} is not a Subtask".format(subtask))

    def remove_subtask(self, subtask):
        if subtask in self.subtasks_:
            self.subtasks_.remove(subtask)
        else:
            raise KeyError("{} is not in Student's Tasks!".format(subtask))
