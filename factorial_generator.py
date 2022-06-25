"""

factorial of a number using generator

"""


def factorial(n):
    a = 1
    fact = 1
    while (a <= n):
        yield fact
        fact = fact * a
        a += 1


f = factorial(10)

for i in f:
    print(i)
