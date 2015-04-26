import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest

from user import User
from student import Student
from task import Task
from subtask import Subtask

class TestUser(unittest.TestCase):

    def test_valid_first_name(self):
        first_name = "FirstName"
        user = User()
        user.first_name = first_name
        self.assertEqual(first_name, user.first_name)

    def test_invalid_first_name(self):
        first_name = ""
        user = User()
        with self.assertRaises(ValueError):
            user.first_name = first_name

    def test_valid_last_name(self):
        last_name = "LastName"
        user = User()
        user.last_name = last_name
        self.assertEqual(last_name, user.last_name)
        
    def test_invalid_last_name(self):
        last_name = ""
        user = User()
        with self.assertRaises(ValueError):
            user.last_name = last_name

    def test_valid_rights(self):
        rights = "administrator"
        user = User()
        user.rights = rights
        self.assertEqual(rights, user.rights)

    def test_invalid_rights(self):
        rights = "GOD"
        user = User()
        with self.assertRaises(ValueError):
            user.rights = rights

class TestStudent(unittest.TestCase):
    
    def test_valid_gender(self):
        gender = "male"
        student = Student()
        student.gender = gender
        self.assertEqual(gender, student.gender)

    def test_invalid_gender(self):
        gender = "shemale"
        student = Student()
        with self.assertRaises(ValueError):
            student.gender = gender

    def test_valid_tasks(self):
        tasks = [Task(), Task(), Task()]
        student = Student()
        student.tasks = tasks
        self.assertEqual(tasks, student.tasks)

    def test_invalid_tasks(self):
        tasks = []
        student = Student()
        with self.assertRaises(ValueError):
            student.tasks = tasks
            
    def test_valid_add_task(self):
        task = Task()
        student = Student()
        student.add_task(task)
        self.assertTrue(task in student.tasks)

    def test_invalid_add_task(self):
        task = ""
        student = Student()
        with self.assertRaises(ValueError):
            student.add_task(task)

    def test_valid_remove_task(self):
        task = Task()
        student = Student()
        student.add_task(task)
        student.remove_task(task)
        self.assertEqual([], student.tasks)

    def test_invalid_remove_task(self):
        task = Task()
        task.title = "First Assignment"
        student = Student()
        student.add_task(task)
        student.remove_task(task)
        with self.assertRaises(KeyError):
            student.remove_task(task)


class TestTask(unittest.TestCase):

    def test_valid_title(self):
        title = "First Lesson"
        task = Task()
        task.title = title
        self.assertEqual(title, task.title)

    def test_invalid_title(self):
        title = ""
        task = Task()
        with self.assertRaises(ValueError):
            task.title = title

    def test_valid_content(self):
        content = "This lesson is about these characters: a, b, c."
        task = Task()
        task.content = content
        self.assertEqual(content, task.content)

    def test_invalid_content(self):
        content = ""
        task = Task()
        with self.assertRaises(ValueError):
            task.content = content

    def test_valid_subtasks(self):
        subtasks = [Subtask(), Subtask(), Subtask()]
        task = Task()
        task.subtasks = subtasks
        self.assertEqual(subtasks, task.subtasks)

    def test_invalid_subtasks(self):
        subtasks = []
        task = Task()
        with self.assertRaises(ValueError):
            task.subtasks = subtasks

    def test_valid_add_subtask(self):
        subtask = Subtask()
        task = Task()
        task.add_subtask(subtask)
        self.assertTrue(subtask in task.subtasks)

    def test_invalid_add_subtask(self):
        subtask = ""
        task = Task()
        with self.assertRaises(ValueError):
            task.add_subtask(subtask)

    def test_valid_remove_subtask(self):
        subtask = Subtask()
        task = Task()
        task.add_subtask(subtask)
        task.remove_subtask(subtask)
        self.assertEqual([], task.subtasks)

    def test_invalid_remove_task(self):
        subtask = Subtask()
        subtask.title = "First Subtask"
        task = Task()
        task.add_subtask(subtask)
        task.remove_subtask(subtask)
        with self.assertRaises(KeyError):
            task.remove_subtask(subtask)

class TestSubtask(unittest.TestCase):

    def test_valid_title(self):
        title = "This is the first subtask"
        subtask = Subtask()
        subtask.title = title
        self.assertEqual(title, subtask.title)

    def test_invalid_title(self):
        title = ""
        subtask = Subtask()
        with self.assertRaises(ValueError):
            subtask.title = title

    def test_valid_content(self):
        content = "This is the first subtask"
        subtask = Subtask()
        subtask.content = content
        self.assertEqual(content, subtask.content)

    def test_invalid_title(self):
        content = ""
        subtask = Subtask()
        with self.assertRaises(ValueError):
            subtask.content = content

    def test_valid_state(self):
        state = "Started"
        subtask = Subtask()
        subtask.state = state
        self.assertEqual(state, subtask.state)

    def test_invalid_state(self):
        state = True
        subtask = Subtask()
        with self.assertRaises(ValueError):
            subtask.state = state

if __name__ == '__main__':
    unittest.main()
