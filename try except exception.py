'''

try except exception handling in python

'''

print("enter the first number ")
num1=input()
print("enter the second number ")
num2=input()

try:
    print("the difference of the two numbers is ", int(num1)-int(num2))

except Exception as e:
    print(e)


print("u did a great jobbb!!!")