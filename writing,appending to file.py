'''
writing and appending to a file

'''
'''
f = open("file1.txt","w")
f.write("taylor swift writes all of her songs ")
f.close()

f=open("file2.txt","a")
f.write("tay tay won artist of the year \n")
f.close()
'''


f= open("file2.txt","a")   #append adds , whatever was previoudly there, it will be plus new ones it adds
a = f.write("taylor swift writes all of her songs ")
print(a)    #returns the number of characters
f.close()

f = open("file2.txt","w")   #it clears the file and then put the text
a = f.write("taylor swift writes all of her songs ")
print(a)
f.close()



