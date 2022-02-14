'''
FOR
'''

#list1 = [["1989",2016], ["reputation",2017], ["lover",2019], ["fearless tv",2021], ["red tv", 2021]]
'''
for album in list1:
    print(album)
'''
#for album,year in list1:
 #   print(album,"and the release year is -> ",year)
'''
printing using a dictionary
dict1 = dict(list1)
print(dict1)

dict1 = dict(list1)
for album,year in dict1.items():
    print(album, "and the year is -> ",year)
'''
#Q1. make a list, and take anything u want , and check if they are numbers and then see if its greater than 6

items = [int, float,"RisiTA",9,4,6,23,56,1,100]

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)
