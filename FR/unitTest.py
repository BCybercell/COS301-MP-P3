import unittest
from FacialRecognition import Log, addClient, deactivateClient, reactivateClient,AuthenticateUser, AuthenticateImage
import datetime as dt
import sys


# Testing Log Function
class TestLog(unittest.TestCase):
    def test_Log_TrueStatus(self):
        self.fail()

    def test_Log_TrueStatus(self):
        self.assertTrue(Log("0",True), "Should be True")

    def test_Log_FalseStatus(self):
        self.fail()

    def test_Log_FalseStatus(self):
        self.assertTrue(Log("0",False), "Should be True")


# class TestGetLog(unittest.TestCase):
#     def test_GetLog_with_value1_no_value2(self):
#         self.fail()
#
#     def test_GetLog_with_value1_no_value2(self):
#         lDate1 = dt.datetime(2019, 3, 12, 18, 00, 00)
#         log = getLog(lDate1)
#
#         self.assertEqual(log['error'], 'Missing end parameter')

# def test_AU_with_multiple_value(self):
#     lDate1 = dt.datetime(2019, 3, 12, 18, 00, 00)
#     lDate2 = dt.datetime(2019, 3, 12, 18, 39, 00)
#     log = getLog(lDate1, lDate2)
#     self.assertFalse(log['error'], "Should be False")
#
# def test_AU_without_value(self):
#     log = getLog()
#     self.assertIsInstance(log['error'], str, "Should be string")

# Testing Add Client Function
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


class TestAuthenticateUser(unittest.TestCase):
    def test_AU_with_value(self):
        self.fail()

    def test_AU_with_value(self):
        self.assertIsInstance(AuthenticateUser('./test1.jpg'), str, "Should be type int")
        self.assertIsInstance(AuthenticateUser('./test4.jpg'), str, "Should be type int")
        self.assertIsInstance(AuthenticateUser('./test3.jpg'), int, "Should be type int")

    def test_AU_without_value(self):
        self.fail()

    def test_AU_without_value(self):
        self.assertEqual(AuthenticateUser(''), -1, "Should be -1")

# Testing Deactivate Client Function
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


class TestAuthenticateImage(unittest.TestCase):
    def test_AI_with_value(self):
        self.fail()

    def test_AI_with_value(self):
        userID = AuthenticateImage('./test1.jpg')
        self.assertIsInstance(userID, str, "Should be type int")

    def test_AI_with_value2(self):
        self.fail()


    def test_AI_with_value2(self):
        userID = AuthenticateImage('./test4.jpg')
        self.assertIsInstance(userID, str, "Should be type int")


    def test_AI_with_value1(self):
        self.fail()


    def test_AI_with_value1(self):
        userID = AuthenticateImage('./test3.jpg')
        self.assertIsInstance(userID, int, "Should be type int")

    def test_AI_without_value(self):
        self.fail()

    def test_AI_without_value(self):
        userID = AuthenticateImage('')
        self.assertEqual(userID, -1, "Should be -1")


# Testing Reactivate Client Function
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
