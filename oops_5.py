'''

class methods in python

'''

class Album:
    no_of_leaves = 8

    def __init__(self, aname, aalbum, ayear):
        self.name = aname
        self.album = aalbum
        self.year = ayear

    def printdetails(self):
        return f"Name is {self.name}. studio album is {self.album} and release year is {self.year}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

harry = Album("Harry Styles", "Fine Line", 2019)
taylor = Album("Taylor Swift", "Reputation", 2017)


harry.change_leaves(34)

print(harry.no_of_leaves)

