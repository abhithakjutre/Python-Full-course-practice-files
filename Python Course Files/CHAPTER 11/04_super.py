class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    super().__init__()  # Call the constructor of Employee
    def __init__(self):
        print("Constructor of Programmer")
    b = 2 

class Manager(Programmer):
    def __init__(self):
        print("Constructor of Manager")
    c = 3
 
o = Employee()
print(o.a)
p = Programmer()
print(p.a, p.b)
m = Manager()
print(m.a, m.b, m.c)