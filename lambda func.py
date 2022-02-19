'''
ANONYMOUS FUNCTIONS OR LAMBDA FUNCTIONS IN PYTHON ->
the main objective of anonymous functions is that, when we need a function just once,
anonymous functions come in handy. Lambda operator is not only used to create anonymous functions,
but there are many other uses of the lambda expression. We can create anonymous functions wherever they are needed.
due to this reason, Python Lambda Functions are also called as throw-away functions which are used
along with other predefined functions such as reduce(), filter(), and map().

These functions help reduce the number of lines of the code when compared to named Python functions.




'''
# def minus(x,y):         #same
#     return x-y
# print(minus(9,4))
#
# minus = lambda x, y: x-y      #same, just represented using lambda function
# print(minus(9,4))

a = [[5,7],[9,4],[1,3]]
def a_first(a):
    return a[1]
a.sort(key=a_first)
print(a)

#representing this with lambda functions
a = [[5,7],[9,4],[1,3]]
a.sort(key=lambda a:a[1])
print(a)