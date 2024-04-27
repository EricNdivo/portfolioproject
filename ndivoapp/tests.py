from http import client
from django.test import TestCase
from django.utils import timezone
import unittest

from .views import login

class TestLogin(unittest.TestCase):

    def test_invalid_login(self):
        self.assertTrue(login("username", "password"))

    def test_invalid_login(self):
        self.assertFalse(login("Wrong_username", "wrong_password"))

if __name__ == '__main__':
    unittest.main()