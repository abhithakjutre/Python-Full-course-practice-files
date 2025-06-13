# 6. Write a program to calculate the factorial of a given number using for loop. 

# 5! = 1 X 2 X 3 X 4 X 5

num = int(input("Enter the number : "))

product = 1 
for i in range(1,num+1): 
    product = product * i

print(f"The factorial of {num} is :{product} ")