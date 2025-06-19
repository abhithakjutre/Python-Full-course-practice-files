
class Employee: 
    language = "Python" # This is a class attribute
    salary = 2200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod   #  decorator to mark greet as a static method 
    def greet():
        print("Good morning")



Abhicoder = Employee()
Abhicoder.language = "JavaScript" # This is instance attribute

Abhicoder.greet()
Abhicoder.getInfo()
# Employee.getInfo(Abhicoder)  