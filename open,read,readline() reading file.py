'''
Open(), Read() & Readline() For Reading File


'''
'''
f = open("file1.txt")
content = f.read()
print(content)
'''
'''
#for character by character read
f = open("file1.txt")
content = f.read()

for line in content:
    print(line)

'''
'''
#for line by line read
f = open("file1.txt","rt")

for line in f:
    print(line, end=" ")

'''
f = open("file1.txt","rt")
# print(f.readline())
# print(f.readline())
# print(f.readline())
print(f.readlines())




f.close()