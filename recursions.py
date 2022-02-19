'''

Recursions: Recursive Vs Iterative Approach

'''

#find factorial of number n in iterative process and recursive method

def fac_iterative(n):
    """
    :param n: integer
    :return: n* n-1* n-2* n-3* .....1
    """
    fac =1
    for i in range(n):
        fac = fac*(i+1)
    return fac

def fac_recursive(n):
    if(n==1):
        return 1
    else:
        return n*fac_recursive(n-1)

# enter the number 5
# 5 * fac_recursive(4)
# 5*4*fac_recursive(3)
# 5*4*3*fac_recursive(2)
# 5*4*3*2*fac_recursive(1)
# 5*4*3*2*1 = 120

num = int(input("enter the number "))
print("factorial of the number using iterative method is ", fac_iterative(num))
print("factorial of the number using recursive method is ", fac_recursive(num))




