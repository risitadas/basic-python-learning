'''
python exercise 3 -->
guess the number:
#number of guesses are limited = 9
#print the number of guesses remanining
#print the number of guesses he took
#game over


'''
n=18
print("the total of 9 guesses are there in this game ")
num_guess=1
while(num_guess<=9):
    x = int(input("enter your guess "))

    if(x>n):
        print("try to go with something smaller ")

    elif(x<n):
        print("try to go with something bigger ")

    else:
        print("u won ")
        print("guesses u took ",num_guess)
        break

    print("no of guesses left ",9-num_guess)
    num_guess=num_guess+1

if(num_guess>9):
    print("game over ")

