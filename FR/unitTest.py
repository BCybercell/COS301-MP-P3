import unittest
from FacialRecognition import Log, getLog
import datetime as dt

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

if __name__ == '__main__':
    unittest.main()
