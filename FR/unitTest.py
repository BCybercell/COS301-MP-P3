import unittest
from .FacialRecognition import AuthenticateUser, AuthenticateImage, Update, Log, getLog
import datetime as dt


class TestAuthenticateUser(unittest.TestCase):
    def test_AuthenticateUser(self):
        self.fail()

    def test_AU_with_value(self):
        self.assertIsInstance(AuthenticateUser('aaaaaaa'), int, "Should be type int")

    def test_AU_with_multiple_value(self):
        self.assertIsInstance(AuthenticateUser(['a', 'b', 'c']), int, "Should be type int")

    def test_AU_without_value(self):
        self.assertEqual(AuthenticateUser(''), -1, "Should be -1")


class TestAuthenticateImage(unittest.TestCase):
    def test_AuthenticateImage(self):
        self.fail()

    def test_AI_with_value(self):
        userID, chance = AuthenticateImage('aaaaaaa')
        self.assertIsInstance(userID, int, "Should be type int")
        self.assertIsInstance(chance, int, "Should be type int")

    def test_AI_without_value(self):
        userID, chance = AuthenticateImage('')
        self.assertEqual(userID, -1, "Should be -1")
        self.assertEqual(chance, 0, "Should be 0")


class TestGetLog(unittest.TestCase):
    def test_GetLog(self):
        self.fail()

    def test_GetLog_with_value1_no_value2(self):
        lDate1 = dt.datetime(2019, 3, 12, 18, 00, 00)
        lDate2 = dt.datetime(2019, 3, 12, 18, 39, 00)
        log = getLog(lDate1)
        self.assertIsInstance(log['error'], str, "Should be string")

    def test_AU_with_multiple_value(self):
        lDate1 = dt.datetime(2019, 3, 12, 18, 00, 00)
        lDate2 = dt.datetime(2019, 3, 12, 18, 39, 00)
        log = getLog(lDate1, lDate2)
        self.assertFalse(log['error'], "Should be False")

    def test_AU_without_value(self):
        log = getLog()
        self.assertIsInstance(log['error'], str, "Should be string")


class TestLog(unittest.TestCase):
    def test_Log(self):
        self.fail()

    def test_Log(self):
        lDate1 = dt.datetime(2019, 3, 12, 18, 00, 00)
        lDate2 = dt.datetime(2019, 3, 12, 18, 39, 00)
        self.assertTrue(Log(1, lDate1, lDate2, True), "Should be True")


class TestUpdate(unittest.TestCase):
    def test_Update(self):
        self.fail()

    def test_Update(self):
        self.assertTrue(Update(), "Should be True")


if __name__ == '__main__':
    unittest.main()
