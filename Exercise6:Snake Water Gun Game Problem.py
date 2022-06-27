'''
SNAKE WATER GUN GAME

 The snake drinks the water, the gun shoots the snake, and gun has no effect on water.

'''
import random
list1 = ['s','w','g']

chance = 10
no_of_chances = 0
computer_score = 0
your_score = 0

print("\n SNAKE , WATER , GUN GAME \n")
print("s for snake , w for water , g for gun ")

while(no_of_chances<chance):
    ch = input('Snake, Water, Gun : ')
    ran_dom = random.choice(list1)

    if(ch==ran_dom):
        print("TIE , both 0 point to each other ")

    elif(ch=='s' and ran_dom=='g'):
        computer_score = computer_score+1
        print(f"your guess {ch} and computer guess {ran_dom} \n")
        print("computer wins 1 point ")
        print(f"your point is {your_score} and computer point is {computer_score} \n")

    elif(ch=='s' and ran_dom=='w'):
        your_score = your_score+1
        print(f"your guess {ch} and computer guess {ran_dom} \n")
        print("you win 1 point ")
        print(f"your point is {your_score} and computer point is {computer_score} \n")

    elif(ch=='w' and ran_dom=='s'):
        computer_score = computer_score+1
        print(f"your guess {ch} and computer guess {ran_dom} \n")
        print("computer win 1 point ")
        print(f"your point is {your_score} and computer point is {computer_score} \n")

    elif(ch=='w' and ran_dom =='g'):
        your_score = your_score+1
        print(f"your guess {ch} and computer guess {ran_dom} \n")
        print("you win 1 point ")
        print(f"your point is {your_score} and computer point is {computer_score} \n")

    elif(ch=='g' and ran_dom =='s'):
        your_score = your_score+1
        print(f"your guess {ch} and computer guess {ran_dom} \n")
        print("you win 1 point ")
        print(f"your point is {your_score} and computer point is {computer_score} \n")

    elif(ch=='g' and ran_dom =='w'):
        computer_score = computer_score+1
        print(f"your guess {ch} and computer guess {ran_dom} \n")
        print("computer 1 point ")
        print(f"your point is {your_score} and computer point is {computer_score} \n")

    else:
        print("please input valid choice  ")

    no_of_chances = no_of_chances+1
    print(f"{chance-no_of_chances} is left out of {chance} \n")

print("Game Over ")

if(computer_score==your_score):
    print("TIE")

elif(computer_score>your_score):
    print("computer wins, and you lose ")

else:
    print("you win, and computer lose")

print(f"your score {your_score} and computer score {computer_score} \n")
