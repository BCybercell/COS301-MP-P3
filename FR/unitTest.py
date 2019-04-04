import unittest
from FacialRecognition import AuthenticateUser, AuthenticateImage
import datetime as dt

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
   
if __name__ == '__main__':
    unittest.main()
