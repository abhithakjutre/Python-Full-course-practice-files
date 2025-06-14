# 2. Write a python program using function to convert Celsius to Fahrenheit. 

def c_to_f(c): 
    return (c * 9/5) + 32




c = int(input("Enter temprature in Celsius : "))
f = c_to_f(c) # This is function call
print(f"{f}°f")

