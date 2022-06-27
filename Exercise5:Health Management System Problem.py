'''
HEATH MANAGEMENT SYSTEM:

3 clients - Harry, Rohan and Hammad

def getdate():
    import datetime
    return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

Ask the user whether they want to log or retrieve client data.
Write a function that takes the user input of the client's name.
After the client's name is entered, it will display a message as "What you want to log- Diet or Exercise".



'''
import datetime
def gettime():
    return datetime.datetime.now()


def take(m):
    if(m==1):
        c = int(input("Enter 1 for Exercise and 2 for Food "))
        if(c==1):
            value = input("enter here ")
            with open("Simon_ex.txt","a") as op:
                op.write(str([str(gettime())]) + " : " + value +" \n ")
            print("sucessfully inputed ")

        elif(c==2):
            value = input("enter here ")
            with open("Simon_food.txt", "a") as op:
                op.write(str([str(gettime())]) + " : " + value + " \n ")
            print("sucessfully written ")

    elif(m==2):
        c = int(input("Enter 1 for Exercise and 2 for Food "))
        if (c == 1):
            value = input("enter here ")
            with open("Baz_ex.txt", "a") as op:
                op.write(str([str(gettime())]) + " : " + value + " \n ")
            print("sucessfully inputed ")

        elif (c == 2):
            value = input("enter here ")
            with open("Baz_food.txt", "a") as op:
                op.write(str([str(gettime())]) + " : " + value + " \n ")
            print("sucessfully written ")

    elif(m==3):
        c = int(input("Enter 1 for Exercise and 2 for Food "))
        if (c == 1):
            value = input("enter here ")
            with open("Rowell_ex.txt", "a") as op:
                op.write(str([str(gettime())]) + " : " + value + " \n ")
            print("sucessfully inputed ")

        elif (c == 2):
            value = input("enter here ")
            with open("Rowell_food.txt", "a") as op:
                op.write(str([str(gettime())]) + " : " + value + " \n ")
            print("sucessfully written ")

    else:
        print("Please enter valid input next time ")

def retrieve(m):
    if(m==1):
        c = int(input("Enter 1 for Exercise and 2 for Food "))
        if(c==1):
            with open("Simon_ex.txt") as op:
                for i in op:
                    print(i , end=" ")
        elif(c==2):
            with open("Simon_food.txt") as op:
                for i in op:
                    print(i , end=" ")

    elif(m==2):
        c = int(input("Enter 1 for Exercise and 2 for Food "))
        if (c == 1):
            with open("Baz_ex.txt") as op:
                for i in op:
                    print(i, end=" ")
        elif (c == 2):
            with open("Baz_food.txt") as op:
                for i in op:
                    print(i, end=" ")

    elif(m==3):
        c = int(input("Enter 1 for Exercise and 2 for Food "))
        if (c == 1):
            with open("Rowell_ex.txt") as op:
                for i in op:
                    print(i, end=" ")
        elif (c == 2):
            with open("Rowell_food.txt") as op:
                for i in op:
                    print(i, end=" ")

    else:
        print("Please enter valid input next time ")

print("HEALTH MANAGEMENT SYSTEM ")
a = int(input("Enter 1 for Log and 2 for Retrieve "))

if(a==1):
    b = int(input("Press 1 for Simon , 2 for Baz , 3 for Rowell "))
    take(b)

else:
    b = int(input("Press 1 for Simon , 2 for Baz , 3 for Rowell "))
    retrieve(b)
