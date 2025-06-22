
class Employee :

    company = "Google "
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "Microsoft"
#     def show(self):
#         print("The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print("The name is {self.name} and the language is {self.language}")

class Programmer(Employee): # This class inherited of the Employee
    company = "Microsoft Programmer"
    def showLanguage(self):
        print(f"The name is {self.name} and the language is {self.language}")


a = Employee()
b = Programmer()

print(a.company,b.company)
    