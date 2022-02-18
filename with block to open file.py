'''
Using With Block To Open Python Files

--> using this, there's no need to close the file, because block handles it
'''

with open("file3.txt") as f:
    a = f.read(11)
    print(a)