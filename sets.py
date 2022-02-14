'''
SETS IN PYTHON
'''

s = set()
#print(type(s))
s1 = set([1,2,3,4,5])
#print(s1)
l=[5,6,7,8]
s2 = set(l)
#print(s2)
#FUNCTIONS
#adding elements
s2.add(9)
s2.add(10)
#print(s2)
#s3 = s2.union({11,12,13,14})
#s4 = s2.intersection({8,9,10,11})
#s5={4,6}
#print(s2.isdisjoint(s5))
s2.remove(8)
print(s2)
