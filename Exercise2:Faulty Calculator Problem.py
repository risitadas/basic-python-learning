'''
FAULTY CALCULATOR PROBLEM
you have to take the operator and the two values from user as inputs and return the correct answers
 except for the following calculations, it will show the wrong one
 45*3=555, 56+9=77.56/6=4

'''

num1 = int(input("enter the first number "))
num2 = int(input("enter the second number "))
op = input("enter the operator : + - * / ^ -->    ")

if(num1 ==45 and num2==3 and op=='*'):
    print("555")
elif(num1==56 and num2==9 and op=='+'):
    print("77")
elif(num1==56 and num2==6 and op=='/'):
    print("4")
elif(op=='+'):
    print(num1+num2)
elif(op=='-'):
    print(num1-num2)
elif(op=='*'):
    print(num1*num2)
elif(op=='/'):
    print(num1/num2)
elif(op=='^'):
    print(num1**num2)
else:
    print("wrong input ")
