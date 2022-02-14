'''
FUNCTIONS AND DOCSTRINGS
built in function
user defined function

'''
'''
a=9
b=7
c=sum((a,b))   #built in function
print(c)

'''

def function1(a,b):            #user defined function
    print("you are in function1 ",a+b)

def function2(a,b):
    avg = (a+b)/2
    return avg

c=function2(7,8)
print(c)

def function3(a,b):
    """This is a function to calculate the average of two numbers
    not for three numbers """
    avg = (a + b) / 2
    return avg

print(function3.__doc__)