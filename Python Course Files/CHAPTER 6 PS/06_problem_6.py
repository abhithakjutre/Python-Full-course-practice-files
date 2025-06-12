# 6. Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50 => F        

percentage  = float(input("Enter the percentage of the student : "))

if(percentage >= 90 and percentage <= 100): 
    print("Ex")

elif(percentage >= 80 and percentage < 90): 
    print("A")

elif(percentage >= 70 and percentage < 80): 
    print("B")

elif(percentage >= 60 and percentage < 70): 
    print("C")

elif(percentage >= 50 and percentage < 60): 
    print("D")

elif("percentage < 50 and percentage >= 0"): 
    print("F")

else: 
    print("Please enter valid percentage try again :)")