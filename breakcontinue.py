'''
break and continue statements

'''
'''
i=0

while(True):
    print(i+1, end=" ")
    if(i==44):
        break
    i=i+1
'''
'''
i=0
while(True):
    if(i+1<5):
        i=i+1
        continue
    print(i+1,end=" ")
    if(i==44):
        i=i+1
        break
    i=i+1
'''
#   q1. take input from the user and keep taking unless it gives a number greater than 100


while(True):
    x = int(input("enter your number "))
    if(x<=100):
        print("keep trying ")
        continue
    else:
        print("congratulations u have reached above 100 ")
        break