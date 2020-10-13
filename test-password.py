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

def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.test_save_user() # saving the new user
        self.assertEqual(len(User.user_list),1) # confirming an addition has been made to the user 









if __name__ == '__main__':
    unittest.main()
