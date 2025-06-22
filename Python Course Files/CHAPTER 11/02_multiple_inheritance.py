
class Employee :

    company = "Google "
    name = "Default name"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the languages here is your language: {self.language}")

class Programmer(Employee,Coder): # This class inherited of the Employee
    company = "Microsoft Programmer"
    def showLanguage(self):
        print(f"The name is {self.name} and the language is {self.language}")


a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()


