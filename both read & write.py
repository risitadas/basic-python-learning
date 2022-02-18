#HANDLE BOTH READ AND WRITE

f = open("file2.txt","r+")          #reads and write
print(f.read())
f.write("ts won the artist of the year ")
