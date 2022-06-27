'''

Self & __init__() (Constructors)

'''

class Album:
    #no_of_leaves = 8

    def __init__(self, aname, aalbum, ayear):
        self.name = aname
        self.album = aalbum
        self.year = ayear

    def printdetails(self):
        return f"Name is {self.name}. studio album is {self.album} and release year is {self.year}"


harry = Album("Harry Styles", "Fine Line", 2019)
taylor = Album("Taylor Swift", "Reputation", 2017)

print(harry.printdetails())
print(taylor.printdetails())
print(harry.year)
print(taylor.album)

