'''

multilevel inheritance

'''

'''
class level1:
    def first(self):
        print('code')


class level2(level1):  # inherit level1
    def second(self):
        print('with')


class level3(level2):  # inherit level2
    def third(self):
        print('harry')


obj = level3()
obj.first()
obj.second()
obj.third()

'''


class Dad:
    basketball =6

class Son(Dad):
    dance =1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance =6
    guitar = 1

    def isdance(self):
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()

#print(darry.guitar)

# electronic device
# pocket gadget
# phone




