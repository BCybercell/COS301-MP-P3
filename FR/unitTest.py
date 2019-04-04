import unittest
from .FacialRecognition import AddImages
import datetime as dt


class TestAddImages(unittest.TestCase):
    def test_AuthenticateUser(self):
        self.fail()

    def test_AI_with_only_id(self):
        self.assertIsInstance(AddImages("1"), bool, "Should return false for error")

    def test_AI_with_multiple_values(self):
        self.assertIsInstance(AddImages("1", "/test.ping"), bool, "Should return true or false depending if found")

    def test_AI_without_values(self):
        self.assertIsInstance(AddImages(), bool, "Should return false for error")

if __name__ == '__main__':
    unittest.main()
