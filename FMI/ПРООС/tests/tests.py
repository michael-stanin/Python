import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest

from user import User

class TestUser(unittest.TestCase):

    def test_first_name(self):
        name = "FirstName"
        user = User()
        user.first_name = name
        self.assertEqual(name, user.first_name)

    def test_last_name(self):
        name = "LastName"
        user = User()
        user.last_name = name
        self.assertEqual(name, user.last_name)


if __name__ == '__main__':
    unittest.main()
