'''
fibonacci series :
0 1 1 2 3 5 8 13 ....n
sum of two previous numbers gives the next number
'''
def fibonacci(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("enter the number upto which u want to calculate "))
print("fibonacci series --> ", fibonacci(num))