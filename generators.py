'''

Iterable - __iter__() or __getitem__()

for c in a:
      print (a)
#Here a is an iterable.

Iterator - __next__()
Iteration -

generators


'''

"""
def gen(n):
    for i in range(n):
        yield i

g = gen(3)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())     #throws an error because its only till 2 as in 0-2

"""

# for i in g:
#     print(i)

h = 'taylor'
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())  #will print all the letters in the word

# for c in h:
#     print(c)
