import unittest
from FacialRecognition import Log, getLog, addClient, deactivateClient, reactivateClient
import datetime as dt
import sys

#Testing Log Function
class TestLog(unittest.TestCase):
    def test_Log_TrueStatus(self):
        self.fail()

    def test_Log_TrueStatus(self):
        self.assertTrue(Log("0",True), "Should be True")

    def test_Log_FalseStatus(self):
        self.fail()

    def test_Log_FalseStatus(self):
        self.assertTrue(Log("0",False), "Should be True")

#Testing Add Client Function
class TestAddClient(unittest.TestCase):
    def test_valid_AddClient(self):
        self.fail()

    def test_valid_AddClient(self):
        userID = 0
        self.assertTrue(addClient(userID), "Should be True")

    def test_invalid_AddClient(self):
        self.fail()

    def test_invalid_AddClient(self):
        userID = -1
        self.assertFalse(addClient(userID), "Should be False")

    def test_valid_high_AddClient(self):
        self.fail()

    def test_valid_high_AddClient(self):
        userID = 500000000000000000000000
        self.assertTrue(addClient(userID), "Should be True")

#Testing Deactivate Client Function
class TestDeactivateClient(unittest.TestCase):
    def test_valid_DeactivateClient(self):
        self.fail()

    def test_valid_DeactivateClient(self):
        userID = 0
        self.assertTrue(deactivateClient(userID), "Should be True")

    def test_invalid_DeactivateClient(self):
        self.fail()

    def test_invalid_DeactivateClient(self):
        userID = -1
        self.assertFalse(deactivateClient(userID), "Should be False")

    def test_valid_high_DeactivateClient(self):
        self.fail()

    def test_valid_high_DeactivateClient(self):
        userID = 500000000000000000000000
        self.assertTrue(deactivateClient(userID), "Should be True")

#Testing Reactivate Client Function
class TestReactivateClient(unittest.TestCase):
    def test_valid_ReactivateClient(self):
        self.fail()

    def test_valid_ReactivateClient(self):
        userID = 0
        self.assertTrue(reactivateClient(userID), "Should be True")

    def test_invalid_ReactivateClient(self):
        self.fail()

    def test_invalid_ReactivateClient(self):
        userID = -1
        self.assertFalse(reactivateClient(userID), "Should be False")

    def test_valid_high_ReactivateClient(self):
        self.fail()

    def test_valid_high_ReactivateClient(self):
        userID = 500000000000000000000000
        self.assertTrue(reactivateClient(userID), "Should be True")

if __name__ == '__main__':
    unittest.main()
