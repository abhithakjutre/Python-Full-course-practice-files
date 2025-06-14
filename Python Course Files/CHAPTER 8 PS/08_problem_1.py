# 1. Write a program using functions to find greatest of three numbers. 

def greatest(a, b, c): 
    if(a>b and b>c): 
        return a
    elif(b>a and b>c): 
        return b
    elif(c>b and c>a): 
        return c
    

a = 1 
b = 23 
c = 5

print(greatest(a, b, c))