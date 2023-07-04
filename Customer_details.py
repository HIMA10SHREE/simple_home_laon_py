import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
class Salary(Exception):
    def salary(self, arg):
           self.msg=arg

class Customer(Salary):

     def __init__(self):
         print("=================WELCOME TO CUSTOMER PAGE======================")
         self.c_name = input("Enter your name:")
         self.c_email = input("Enter your email:")
         self.c_account = input("Enter your Bank account number:")
         self.c_address = input("Enter your residential address:")

     def my_func(self):
         global c_EMI,c_loan
         c_sal = int(input("Enter your salary"))
         if c_sal < 30000:
             raise Salary("Your are not applicable for Home Loan")
         else:
             print("Continue further process............")

         # inpu = int(input("Enter upto how many years you want to take loan:")
         if c_sal>=30000 or c_sal<60000:
             inpu=int(input("Enter upto how many years you want to take loan:"))
             c_EMI= c_sal * 0.30
             c_loan=12*inpu*c_EMI
             print("===========The Customer Loan Details are============== ")
             print("Your House loan for {} years is {}:".format(inpu,c_loan))
             print("Your EMI for the month is:",c_EMI)


         else:
             inp=int(input("Enter upto how many years you want to take loan:"))
             c_EMI = c_sal * 0.50
             c_loan = 12 * inp * c_EMI
             print("=============The Customer Loan Details are ===================")
             print("Your House loan for {} years is {}:".format(inp, c_loan))
             print("Your EMI for the month is:", c_EMI)

     def get_details(self):
        print("Customer name is ", self.c_name)
        print("Customer email/phone is ", self.c_email)
        print("Customer account is ", self.c_account)
        print("Customer address is ", self.c_address)


# cust=Customer()
# cust.my_func()
# # cust.get_details()