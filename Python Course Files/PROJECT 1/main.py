
import random
'''
1 for snake
-1 for water 
0 for gun

'''

computer = random.choice([1 , -1 , 0])
youstr = input("Enter your choice : ")
youDict = {"s":1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

print(f"You chose { reverseDict[you]}\nComputer chose {reverseDict[computer] }")
if(computer == you): 
    print("Its Draw ")

else:  
    if(computer == -1 and you==1):
        print("You Win :) 🏆")
    elif(computer == -1 and you==0):
        print("You Lose :( 😥")
    elif(computer == 1 and you==-1):
        print("You Lose :( 😥")
    elif(computer == 1 and you==0):
        print("You Win :) 🏆")
    elif(computer == 0 and you==-1):
        print("You Win :) 🏆")
    elif(computer == 0 and you==1):
        print("You Lose :( 😥")

    else: 
        print("Someting went worng!")





