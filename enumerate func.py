'''

Enumerate function in python

'''

list1 = ["1989", "lover", "speak now", "fearless", "reputation","evermore", "debut"]

#
# i=1
# for item in list1:
#     if(i%2!=0):     #if i%2 is not 0 :
#         print(f"this album is being re-recorded {item} ")
#     i+=1

for index,item in enumerate(list1):     #index- starts from 0
    if index%2==0:
        print(f"this album is being re-recorded {item} ")