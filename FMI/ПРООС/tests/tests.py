import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest

from user import User
from student import Student

class TestUser(unittest.TestCase):

    def test_valid_first_name(self):
        first_name = "FirstName"
        user = User()
        user.first_name = first_name
        self.assertEqual(first_name, user.first_name)

    def test_invalid_first_name(self):
        first_name = ""
        user = User()
        user.first_name = first_name
        self.assertIsNone(user.first_name)

    def test_valid_last_name(self):
        last_name = "LastName"
        user = User()
        user.last_name = last_name
        self.assertEqual(last_name, user.last_name)
        
    def test_valid_last_name(self):
        last_name = ""
        user = User()
        user.last_name = last_name
        self.assertIsNone(user.last_name)

    def test_valid_rights(self):
        rights = "administrator"
        user = User()
        user.rights = rights
        self.assertEqual(rights, user.rights)

    def test_invalid_rights(self):
        rights = "GOD"
        user = User()
        user.rights = rights
        self.assertIsNone(user.rights)

class TestStudent(unittest.TestCase):
    
    def test_valid_gender(self):
        gender = "male"
        student = Student()
        student.gender = gender
        self.assertEqual(gender, student.gender)

    def test_invalid_gender(self):
        gender = "shemale"
        student = Student()
        student.gender = gender
        self.assertIsNone(student.gender)
        
if __name__ == '__main__':
    unittest.main()
