import unittest # Importing the unittest module
from password import User # Importing the password class
import uuid
import random
from credentials import Credential


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
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1) # confirming an addition has been made to the user 

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''

        self.new_user.save_user()
        test_user = User("Susan", "Kariuki", "SKaris","SueKaris123")
        test_user.save_user()   #saving a user object
        self.assertEqual(len(User.user_list), 2)

    def delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Susan", "Kariuki", "SKaris","SueKaris123") # new user
            test_user.save_user()

            User.user_list.remove(self)# Deleting a user object
            self.assertEqual(len(User.user_list), 1)

    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by username and display information
        '''

        self.new_user.save_user()
        test_user = User("Susan", "Kariuki", "SKaris","SueKaris123")
        test_user.save_user()

        found_user = User.find_user_by_username("SKaris")

        self.assertEqual(found_user.username,test_user.username) 

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''
        self.new_user.save_user()
        test_user = User("Susan", "Kariuki", "SKaris","SueKaris123")
        test_user.save_user()
        
        user_exists = User.user_exist("SKaris")

        self.assertTrue(user_exists)       

    class TestCredential(unittest.TestCase):
        def setUp(self):
            '''
            Set up method to run before each test cases.
            '''
            self.new_credential = Credential('Susan','Kariuki','Instagram','SKaris','SueKaris123')


        def test_init(self):
            '''
            test_init test case to test if the object is initialized properly
            '''
            self.assertEqual(self.new_credential.first_name,"Susan")
            self.assertEqual(self.new_credential.second_name,"Kariuki")
            self.assertEqual(self.new_credential.account,"Instagram")
            self.assertEqual(self.new_credential.username,"SKaris")
            self.assertEqual(self.new_credential.password, "SueKaris123")
            
        def test_save_credential(self):
            '''
            test_save_credential test case to test if the user object is saved into
            the credential list
            '''
            self.new_credential.save_credential() # saving the new credential
            self.assertEqual(len(Credential.credential_list),1)

        def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []  

        def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential('Susan','Kariuki','Instagram','SKaris','SueKaris123')   # new credential
            test_credential.save_credential()  # saving a credential object
            self.assertEqual(len(Credential.credential_list),2)   

        def test_delete_credential(self):
            '''
            test_delete_credential to test if we can remove a credential from our credential list
            '''
            self.new_credential.save_credential()
            test_credential = Credential('Susan','Kariuki','Instagram','SKaris','SueKaris123')    # new credential
            test_credential.save_credential()

            self.new_credential.delete_credential()     # Deleting a credential object
            self.assertEqual(len(Credential.credential_list),1)

        def test_find_credential_by_username(self):
            '''
            test to check if we can find a credential by username and display information
            '''
            self.new_credential.save_credential()
            test_credential = Credential('Susan','Kariuki','Instagram','SKaris','SueKaris123') # new credential
            test_credential.save_credential()

            found_credential = Credential.find_by_username('SKaris')

            self.assertEqual(found_credential.username,test_credential.username)   

        def test_credential_exists(self):
            '''
            test to check if we can return a Boolean  if we cannot find the credential.
            '''
            self.new_credential.save_credential()
            test_credential = Credential('Susan','Kariuki','Instagram','SKaris','SueKaris123') # new credential
            test_credential.save_credential()

            credential_exists = Credential.credential_exist('SKaris')

            self.assertTrue(credential_exists)






if __name__ == '__main__':
    unittest.main()
