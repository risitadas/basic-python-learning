'''
Single Inheritance

'''
'''

class Parent():
    def first(self):
        print('Parent function')


class Child(Parent):
    def second(self):
        print('Child function')


object1 = Child()
object1.first()
object1.second()
'''


class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


class Programmer(Employee):
    no_of_holiday = 56
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages


    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary}" \
               f" and role is {self.role}.The languages are {self.languages}"



baz = Employee("Baz", 255, "Instructor")
simon = Employee("Simon", 455, "Student")

penelope = Programmer("Penelope", 555, "Programmer", ["python"])
Warner = Programmer("Warner", 777, "Programmer", ["python", "Cpp"])
print(Warner.no_of_holiday)

