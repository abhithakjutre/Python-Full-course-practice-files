
import random
'''
1 for snake
-1 for water 
0 for gun

'''
def game_main():
    score = 0
    win_score = 0
    maxscore = 0

    computer = random.choice([1 , -1 , 0])
    youstr = input("Enter your choice : ")
    youDict = {"s":1, "w": -1, "g": 0}
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

    you = youDict[youstr]

    print(f"You chose { reverseDict[you]}\nComputer chose {reverseDict[computer] }")
    if(computer == you): 
        print("Its Draw ")

    else:  
        if(computer == -1 and you==1) or(computer == 1 and you==0) or(computer == 0 and you==-1) :
            print("You Win :) 🏆")
            score = score + 1
            with open("score.txt", "w") as file:
                file.write(f"score = {score}") 

        elif(computer == 1 and you==-1):
            print("You Lose :( 😥")
       

        else: 
            print("Someting went worng!")


continue_game = input("Enter P to play C to continue to game :")

if(continue_game == "P"):
    game_main()

elif(continue_game == "C"):
    with open("score.txt"," ") as f:
        

else: 
    print("you press wronge key so please enter valid key")




