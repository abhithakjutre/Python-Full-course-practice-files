# Q : 1 Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

abhishek = Programmer("Abhishek Thakur",30000,202398)
print(abhishek.company,abhishek.name,abhishek.salary,abhishek.pincode)
rohan = Programmer("Rohan Thakur",33000,202300)
print(rohan.company,rohan.name,rohan.salary,rohan.pincode)