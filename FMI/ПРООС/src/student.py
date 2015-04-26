from user import User
from task import Task

class Student(User):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tasks_ = []
        self.gender_ = ""
        
    @property
    def gender(self):
        return self.gender_

    @gender.setter
    def gender(self, value):
        if value in ("Male", "Female"):
            self.gender_ = value
        else:
            raise ValueError(
                "{} is not possible value for Gender!".format(value))
    @property
    def tasks(self):
        return self.tasks_

    @tasks.setter
    def tasks(self, value):
        if isinstance(value, list) and value:
            self.tasks_ = value
        else:
            raise ValueError("Tasks for Student are empty!")
        
    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks_.append(task)
        else:
            raise ValueError("{} is not a Task".format(task))

    def remove_task(self, task):
        if task in self.tasks_:
            self.tasks_.remove(task)
        else:
            raise KeyError("{} is not in Student's Tasks!".format(task))
