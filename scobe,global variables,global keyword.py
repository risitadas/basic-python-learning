'''

SCOPE , GLOBAL VARIABLES AND GLOBAL KEYWORD

'''
l = 10  #glabal variable
def func1(n):
    l=5     #local
    m=8     #local
    print(l,m)
    print(n, "i got myself printed ")

func1("this is me")
# print(l)
'''
l = 10
def func1(n):
    #l=5     #local
    m=8     #local
   # l = l+46    #shows error,as l is a glabal variable, and 
                # inside if not found a local variable,it will tey to be in read only mode
    print(l,m)
    print(n, "i got myself printed ")

func1("this is me")
'''
l = 10  #glabal variable
def func1(n):

    m=8     #local
    global l    #glabal keyword
    l=l+87
    print(l,m)
    print(n, "i got myself printed ")

func1("this is me")

'''
x=89
def func2():
    x=20
    def func3():
        global x
        x=34
    func3()
    print("after calling func3 ", x)

func2()
print(x)
'''


