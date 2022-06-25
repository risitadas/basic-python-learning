'''
Else & Finally In Try Except

else keyword --->

try:
    #Run this code
except Exception as error:
    #Execute this code when there is an exception
else:
    #No Exception. Run this code

finally -->

try:
    #Run this code
except Exception as error:
    #Execute this code when there is an exception
else:
   #No Exception. Run this code
finally:
   #Always run this code


'''

def divide(a, b):
    try:
        print(f'{a}/{b} is {a / b}')
    except ZeroDivisionError as e:
        print(e)
    else:
        print("No Exception")
divide(1, 2)

"""

In the try block, all the statements are executed until an exception occurs.
Except block is used to catch and handle the exception(s) that occurs during the execution of the try block.
Else block runs only when no exceptions occur in the execution of the try block.
Finally block always runs; either an exception occurs or not.

"""


f1 = open("file5.txt")

try:
    f = open("file4.py")

except EOFError as e:
    print("Print eof error came ", e)

except IOError as e:
    print("Print IO error came ", e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    # f.close()
    f1.close()

print("Important stuff")
