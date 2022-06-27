'''
input = integer n
boolean = 0/1, true or false

true:               false:
*                   ****
**                  ***
***                 **
****                *

'''
n_rows = int(input("enter the number of rows "))
print("enter 0 or 1 ")
boolean_value = input("0 for false and 1 for true : ")

if(boolean_value=="1"):
    for i in range(0,n_rows):
         for j in range(0,i+1):
            print("*", end=" ")

         print("")

else:

    for i in range(0,n_rows):
          for j in range(n_rows,i,-1):
              print("*", end=" ")

          print("")
