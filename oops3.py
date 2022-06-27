'''

Instance & Class Variables

'''
class Employee:
    no_of_leaves = 8
    pass

risita = Employee()
ishita = Employee()

risita.name = "Risita Das"
risita.salary = 455
risita.role = "creative writer"

ishita.name = "Ishita Mukhopadhyaee"
ishita.salary = 4554
ishita.role = "content writer"

print(Employee.no_of_leaves)
print(Employee.__dict__)
print(risita.__dict__)
Employee.no_of_leaves = 9
print(Employee.__dict__)
print(ishita.__dict__)
print(Employee.no_of_leaves)


