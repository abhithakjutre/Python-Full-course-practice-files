class Employee:
    a = 1 
    @classmethod
    def show(cls):
        print(f"The class attribute of a value is {cls.a}")

e = Employee()
e.a = 45 # Change the class variable
e.show()  # Output: The class is value is 2