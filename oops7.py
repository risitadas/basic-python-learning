'''

Static methods in python

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

    @classmethod
    def from_dash(cls,string):
        # conan = string.split("-")
        # print(conan)
        # return cls(conan[0], conan[1], conan[2])
        return cls(*string.split("-"))

    @staticmethod
    def print_artists(string):
        print("artist is " + string)


harry = Album("Harry Styles", "Fine Line", 2019)
taylor = Album("Taylor Swift", "Reputation", 2017)
conan = Album.from_dash("Conan Gray-Jigsaw-2022")

Album.print_artists("taylor")
