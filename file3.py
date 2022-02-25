
def fun1(str):
    return f"this is to show __name__ {str}"

def sum(num1, num2):
    return num1+num2+13

print("the file being imported is ", __name__)

if __name__=='__main__':        #so that in the time of importing, this wont be shown

    print(fun1("='__main__' in python "))
    a = sum(1,12)
    print(a)
