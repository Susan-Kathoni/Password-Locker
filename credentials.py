class Credential:
    """
    Class that generates new instances of credential
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
