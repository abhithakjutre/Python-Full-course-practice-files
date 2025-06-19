class Employee: 
    language = "Python" # This is a class attribute
    salary = 2200000

    def __init__(self,name,salary,language): # dunder method which is autmatically called

        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod   #  decorator to mark greet as a static method 
    def greet():
        print("Good morning")


abhi = Employee("Yash Thakur", 130000,"Javascript")
# abhi.name = "Abhishek Thakur"
print(abhi.name,abhi.language,abhi.salary)

# yash = Employee() # when i creating an object and dunder method again run

