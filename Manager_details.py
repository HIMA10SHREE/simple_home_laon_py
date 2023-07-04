class Manager_details:
    def __init__(self):
        self.list1 = []

    def inputt(self, bank_name, bank_location, manager_name, manager_id):
        self.bank_name=bank_name
        self.bank_location=bank_location
        self.manager_name=manager_name
        self.manager_id=manager_id
    def save(self):
        self.list1.append([self.bank_name, self.bank_location, self.manager_name, self.manager_id])

    def get_details(self):
        for i in self.list1:
            print("Bank name is:", i[0])
            print("Bank location is:", i[1])
            print("Manager name is:", i[2])
            print("Manager id is:", i[3])
            print(sep=" \n")

    def funfilter(self, string):
        # print(self.list1)
        for i in self.list1:
            if string in i:
                print("Bank name is:", i[0])
                print("Bank location is:", i[1])
                print("Manager name is:", i[2])
                print("Manager id is:", i[3])

                print(sep=" \n")

a=Manager_details();


def addall():
    a.inputt('HDFC', "Christan Basti", 'Ram Prasad', 'R12')
    a.save()
    a.inputt('HDFC', "Ganeshguri", 'Shweta Tiwari', 'ST12')
    a.save()
    a.inputt('ICICI', "Christan Basti", 'George Duke', 'GD33')
    a.save()
    a.inputt('ICICI', "Zoo Road", 'Lovely Singh', 'LS23')
    a.save()
    a.inputt('LIC', "Christan Basti", 'Somnath Sarkar', 'SS45')
    a.save()
    a.inputt('LIC', "Paanbazar", 'Queen Shah', 'QS-09')
    a.save()



# addall()
# #a.get_details()
# print("Filter")


def funmain():
    inpu = True
    global inp
    while inpu:
        print("1.Search by Bank Name")
        print("2.Search by Location ")
        choice = int(input("Enter option:"))
        if choice == 1:
            inp = input("Enter Bank name:")
            a.funfilter(inp)
        elif choice == 2:
            inp = input("Enter location:")
            a.funfilter(inp)
        print("\nDo u want to search again[yes/no]")
        bp = input()
        if bp == 'yes':
            funmain()
        elif bp == 'no':
            inpu = False
# funmain()
