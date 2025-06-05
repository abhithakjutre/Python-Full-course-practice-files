age = int(input("Enter your age: ")) 


# If elif else ladder example 
if(age>=18): 
    print("You are above the age of consent.")
    print("This is for you")

elif(age<0): 
    print("You are entering an invalid age. ")

elif(age==0):
    print("you are entering 0 which is not a valid age.")

else : 
   print("You are below the age of consent.")


print("Thank you for run the program.")