'''

Setters & Property Decorators

'''

'''
@property
 #def getter method

Use @property along with the getter method to access the value of the attribute.


@function_name.setter
#def function

@function_name.setter is a setter method with which we can set the value of the attribute


# Deleter method 
@function_name.deleter

@function_name.deleter is a deleter method which can delete the assigned value by the setter method

'''


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@risita.eefffff.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@risita.eefffff.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


rcb_supporter = Employee("rcb", "Supporter")
# nikhil_raj_pandey = Employee("risita", "eefffff")

print(rcb_supporter.email)

rcb_supporter.fname = "india"

print(rcb_supporter.email)
rcb_supporter.email = "this.that@risita.eefffff.com"
print(rcb_supporter.fname)

del rcb_supporter.email
print(rcb_supporter.email)
rcb_supporter.email = "risita.das@risita.eefffff.com"
print(rcb_supporter.email)

