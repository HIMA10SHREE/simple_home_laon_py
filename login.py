from Registration_page import *
from Customer_details import *

class login(email,Customer):
    def __init__(self, email="", password=""):
        super().__init__()
        self.email = email
        self.password = password

    def set_email(self):
        while True:
            email = input("Enter phone/email:")
            if email in list:
                self.email = email
                break
            elif email not in list:
                print("It is not a registered email or phone number ")
                break
            else:
                print("unmatched email")

    def set_password(self):
        while True:
            password = input("Enter password:")
            if password in list:
                self.password = password
                break
            else:
                print("unmatched password")


# call=login()
#
#
# #e=email()
# call.my_func()
# call.checknum()
# call.checkpassword()
# #print("\n\n")
# print("Welcome to Login_Page".center(60,'*'))
# call.set_email()
# call.set_password()