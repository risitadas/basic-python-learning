'''
F-Strings & String Formatting In Python


'''
'''
#one format
me = "risita"
a = "this is %s"%me
print(a)
'''
'''
#another format
me = "taylor"
a1 = 13
a = "this is %s %s"%(me,a1)
print(a)
'''
'''
#another format
me = "taylor"
a1 = 13
a = "this is {} {}"
b = a.format(me,a1)
print(b)
'''
import math
#f string

me = "taylor "
me1 = "and welcome to the reputation world tour "
a1 =  2.55
me2 = "million of u"
a = f"hey,i am {me}{me1}{a1} {me2} }"
print(a)