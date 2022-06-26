'''

Oh Soldier Prettify My Folder Problem

Problem Statement:
The task you have to perform is "Oh Soldier, Prettify my Folder."

Suppose you have a folder, and its path is also given. You have to create a function that
takes three input arguments,which are:
        def soldier("C://", "harry.txt", "jpg")

i) Full path of the folder as input strings.
ii) Dictionary file
iii) File Format

The function will perform three tasks:

i) First, it will check all the files present in the folder whose paths are given as an input argument.

ii) Then it will capitalize the first letter of each file.
If the file's name is present in a dictionary file, then it will not capitalize the first letter.
It will only capitalize the first letter of the files, which are not present in the dictionary file.

iii) The function renames the file names to numbers in the range of 1 to 100
whose format is the same as mentioned in the input parameter like 1.jpg.
After performing these tasks, your folder will be prettified as all the first letters of the files
will be capitalized except for those whose names are present in the dictionary file.
And the files having the same format as given in the input argument will rename to number in the range of 1-100.


'''


import os


def soldier(path, file_name, file_extension):
    os.chdir(path)

    with open(file_name) as f:
        text = f.read().split("\n")

    # print(text)
    # print(os.listdir())
    i = 1
    for item in os.listdir():

        if item not in text:
            os.rename(item, item.capitalize())

        if item.endswith(file_extension):
            os.rename(item, f'{i}{file_extension}')
            i += 1


if __name__ == '__main__':
    path = input('Give the path name here:')
    file_name = input('Give the file name here:')
    file_extension = input('Give the file extension here:')
    soldier(path, file_name, file_extension)