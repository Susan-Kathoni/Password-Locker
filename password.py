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
    def find_user_by_name(cls,first_name,second_name):

        '''
        Method that takes in a first_name and second_name and returns a user that matches that name.

        Args:
            first_name: first_name to search for
            second_name: second_name to search for
        Returns :
            User that matches the name.
        '''
        for user in cls.user_list:
            if user.name == name:
                return user
   
