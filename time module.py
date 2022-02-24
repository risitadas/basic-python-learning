'''
time module in python

'''

import time

initial = time.time()

k = 0
while (k < 10):
    print("This is risita")
   # time.sleep(2)   #the program stops for 2 seconds
    k += 1
print("While loop ran in", time.time() - initial, "Seconds")

initial2 = time.time()
for i in range(10):
    print("This is risita")
print("For loop ran in", time.time() - initial2, "Seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

