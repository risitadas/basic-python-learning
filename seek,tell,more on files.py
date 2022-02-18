'''

seek(), tell() and more on python files

'''

f = open("file3.txt")
#print(f.tell())     #tells u where the f (file handle) is ,which character
print(f.readline())
f.seek(11)           #change the position of the File Handle to a given specific position
#print(f.tell())
print(f.readline())
#print(f.tell())

f.close()
