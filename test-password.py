import unittest # Importing the unittest module
from password import User # Importing the password class
import uuid
import random


class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the User class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

 def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Susan","Kariuki","SKaris","SueKaris123") # create user object

def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Susan")
        self.assertEqual(self.new_user.second_name,"Kariuki")
        self.assertEqual(self.new_user.username,"SKaris")
        self.assertEqual(self.new_user.password,"SueKaris123")
