import unittest
from FacialRecognition import Log, getLog, addClient
import datetime as dt
import sys

#Testing Log Function
class TestLog(unittest.TestCase):
    def test_Log_TrueStatus(self):
        self.fail()

    def test_Log_TrueStatus(self):
        lStart = dt.datetime(2019, 3, 12, 18, 00, 00)
        lEnd = dt.datetime(2019, 3, 12, 18, 39, 00)
        self.assertTrue(Log(0, lStart, lEnd, True), "Should be True")

    def test_Log_FalseStatus(self):
        self.fail()

    def test_Log_FalseStatus(self):
        lStart = dt.datetime(2019, 3, 12, 18, 00, 00)
        lEnd = dt.datetime(2019, 3, 12, 18, 39, 00)
        self.assertTrue(Log(1, lStart, lEnd, False), "Should be True")

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

if __name__ == '__main__':
    unittest.main()
