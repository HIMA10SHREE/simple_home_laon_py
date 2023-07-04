from Customer_details import *
from login import *
from Manager_details import *
class HomePage(login,Manager_details):

    def __init__(self):
       # super().__init__()
        print("===================Welcome to Home Loan=====================")
        check=True
        while(check):
            print("==================WELCOME TO HOME PAGE================")
            print("1.Register for Home Loan:")
            print("2.Check list of managers available for Home Loan:")
            print("3.Terms and COnditions")
            print("4.Logout")
            choice=int(input("Chooose a option to continue:"))
            if (choice == 1):
                call = login()

                # e=email()
                call.my_func()
                call.checknum()
                call.checkpassword()
                # print("\n\n")
                print("Welcome to Login_Page".center(60, '*'))
                call.set_email()
                call.set_password()
                cust = Customer()
                cust.my_func()
                cust.get_details()
            elif choice == 2:
             #   a = Manager_details()
                addall()
                print("Filter")
                funmain()
                # a.get_details()


            elif choice ==3:
                f=open("tnc.txt",'r')
                data=f.read()
                print(data)
                print('\n')
            elif choice == 4:
                check=False

h=HomePage()