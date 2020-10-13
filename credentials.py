class Credential:
    """
    Class that generates new instances of a credential
    """
    credential_list=[]

    def __init__(self, first_name, second_name, account, username, password):
        self.first_name = first_name
        self.second_name = second_name
        self.account = account
        self.username = username
        self.password = password    

    def save_credential(self):
    
        """
        save_user method saves credential objects into credential_list
        """
    
        Credential.credential_list.append(self)
        
    def delete_credential(self):

        """
        delete_credential method deletes a saved credential from the credential_list
        """

        Credential.credential_list.remove(self)    

    @classmethod
    def find_by_username(cls,username):
        """
        Method that takes in a username and returns a credential that matches that username.

        Args:
            username:  username to search for
        Returns :
            Credential that matches the username.
        """

        for credential in cls.credential_list:
            if credential.username == username:
                return credential  
     
    @classmethod
    def credential_exist(cls,username):
        """
        Method that checks if a credential exists from the credential list.
        Args:
            username: username to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        """
        for credential in cls.credential_list:
            if credential.username == username:
                    return True

        return False       

    @classmethod
    def display_credentials(cls):
        """
        method that returns the credential list
        """
        return cls.credential_list   