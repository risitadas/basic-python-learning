'''

decorators in python

'''

'''
 def function1():
     print("this is folklore album")

 func2 = function1
 del function1
 func2()
'''
'''
 def funcret(num):
     if num==0:
         return print
     if num==1:
         return sum

 a = funcret(1)
 print(a)
'''

# def executor(func):
#     func("this")
#
#
# executor(print)

def dec1(func1):
    def nowplay():
        print("playing now")
        func1()
        print("played")

    return nowplay


@dec1
def album_folklore():
    print("illicit affairs is a good song")


# album_folklore = dec1(ablum_folklore)

album_folklore()



