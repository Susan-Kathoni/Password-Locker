#!/usr/bin/env python3.8
from password import User
from credentials import Credential
import uuid
import random
import getpass
import string

def create_user(first_name,second_name,username,password):
    '''
    Function to create a new user
    '''
    new_user = User(first_name, second_name, username, password)
    return new_user

def save_users(user):
    '''
    Function to save users
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(username):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_user_by_username(username)

def check_existing_users(username):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return User.user_exist(username)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def create_credential(first_name, second_name, account, username, password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(first_name, second_name, account, username, password)
    return new_credential

def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()

def delete_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

def find_credential(username):
    '''
    Function that finds a credential by username and returns the credential
    '''
    return Credential.find_by_username(username)

def check_existing_credentials(username):
    '''
    Function that check if a credential exists with that username and return a Boolean
    '''
    return Credential.credential_exist(username)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()

def generate_password(user):
    """
    Function to generate random password for user
    """
    return user.generate_random_password()

def main():
    print("Welcome to password locker. Please enter your username.")
    username = input()

    ask = input(f"{username}, do you have an account? yes or no > ")

    if ask == "no":
        print("Please create your password locker account now.")
        first_name =input("Enter first_name ")
        second_name = input("Enter second_name > ")
        create = input(
            f"{username}, do you want autogenerated password? yes or no > ")
        if create == "no":
            print("Generate your password.")
            getpass.getpass()
            print("You have successfully created your password locker account.")

        while True:
            print("""
            Use the short codes: cc to create new credential
                                 dc to display credentials
                                 fc to find credential
                                 del to delete credential
                                 rp to generate random password
                                 ex to exit
                                 """)
            short_code = input("Navigate now using the short-codes > ")

            if short_code == "cc":
                print("Create new account")
                print("-"*12)

                print("Enter your name(s)")
                first_name = input("> ")
                second_name = input("> ")

                print("Enter account for example instagram, snapchat....")
                account = input("> ")

                print("Enter your preffered username")
                username = input("> ")

                print("Enter password")
                password = ("> ")
                import pdb; pdb.set_trace()
                # save_credential(create_credential(first_name, second_name, account, username, password)
                # print("\n")
                
                print(f"New credential Name:{first_name},{second_name}, account:{account}, and password:{password} have been created")
                print("\n")

            elif short_code == "rp":
                print("Please enter the account to generate password for > ")
                account = input("Enter accounttype > ")

                def random_password(string_length):
                    letters = string.ascii_letters
                    return "".join(random.choice(letters) for i in range(string_length))

                print(
                    f"Your password for {account} is: ", random_password(10))

            elif short_code == "dc":

                if display_credentials():
                    print("Credentials and passwords")
                    for credential in display_credentials():
                        print(
                            f"Name:{credential.first_name} {credential.second_name} Account:{credential.account} Username:{credential.username} Password:{password}.")
                        print("\n")
                else:
                    print(
                        "No credentials")
                    print("\n")

            elif short_code == 'fc':

                print("Search for username")

                search_username = input()
                if check_existing_credentials(search_username):
                    search_credential = find_credential(search_username)
                    print(
                        f"{search_credential.account} {search_credential.username}")
                    print('-' * 25)

                    print(f"Account password {search_credential.password}")

                else:
                    print(" Username does not exist")

            elif short_code == "del":
                print("Enter username to delete.")
                my_delete = input("> ")
                my_del = find_credential(my_delete)
                delete_credential(my_del)
                print(
                    f" Credential with {my_delete} has been successfully deleted.")

            elif short_code == "ex":
                print("Logged out")
                break

    elif ask == "yes":
        print("Please enter your username and password to login")
        username = input("Username > ")
        password = getpass.getpass()

        while True:
            print("""
                    Use these short codes: 
                                 cc to create new credential
                                 dc to display credential
                                 fc to find credential
                                 del to delete credential
                                 rp to generate random password
                                 ex to exit
                                 """)
            short_code = input("Navigate now using the short-codes > ")

            if short_code == "cc":
                print("Create new account")
                print("-"*12)

                print("Enter your first_name and second_name.")
                first_name = input("> ")
                second_name = input("> ")

                print("Enter account; for example facebook, instagram...")
                account = input("> ")

                print("Enter you preffered username...")
                username = input("> ")

                print("Enter password")
                password = input("> ")

                save_credential(create_credential(
                   first_name, second_name, account, username, password))

                print("\n")
                print(
                    f"New credential Name:{first_name}, {second_name}, Account:{account}, username:{username}, Password:{password} have just been created!")

            elif short_code == "rp":
                print(
                    "Which account do you want an autogenerated password for? > ")
                account = input("Account > ")

                def random_password(string_length):
                    letters = string.ascii_letters
                    return "".join(random.choice(letters) for i in range(string_length))

                print(f"Your {account} password is: ", random_password(10))

            elif short_code == "dc":

                if display_credentials():
                    print("Credentials and passwords")
                    print("\n")
                for credential in display_credentials():
                    print(
                        f"Name:{first_name}, {second_name}, Account:{credential.account}, Username:{credential.username}, and password:{password}")
                else:
                    print("\n")
                    print("No saved credentials yet.")

            elif short_code == 'fc':

                print("Enter the username")

                search_username = input()
                if check_existing_credentials(search_username):
                    search_credential = find_credential(search_username)
                    print(
                        f"{search_credential.account} {search_credential.username}")
                    print('-' * 25)

                    print(f"Account password {search_credential.password}")

                else:
                    print("That credential does not exist")

            elif short_code == "del":
                print("Enter the username you want to delete.")
                my_delete = input()
                my_del = find_credential(my_delete)
                Credential.credential_list.remove(my_del)
                print(f"{my_delete} has been successfully deleted.")

            elif short_code == "ex":
                print("Logged out")
                break
            else:
                print("Please check your input")


if __name__ == '__main__':
    main()
