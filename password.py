class User:

    """
    Class that generates new instances of users.
    """

    user_list = []
    def __init__(self,first_name,second_name,username,password):
        self.first_name = first_name
        self.second_name = second_name
        self.username = username
        self.password = password

    def save_user(self):

        """
        save_user method saves user objects into user_list
        """

        User.user_list.append(self) 

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)    

    @classmethod
    def find_user_by_username(cls,username):

        '''
        Method that takes in a username and returns a user that matches that username.

        Args:
            username: username to search for
        Returns :
            User that matches the username.
        '''
        for user in cls.user_list:
            if user.username == username:
                return user

    @classmethod
    def user_exist(cls,username):
        '''
        Method that checks if a user exists from the user list.
        Args:
            username: username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.username == username:
                    return True

        return False   

   
