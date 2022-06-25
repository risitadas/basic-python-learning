'''

Function Caching in Python

Caching means storing the data in a place from where it can be served faster.
In the case of data that has been frequently used, the computer assigns a cache memory,
so it does not have to load it again and again from the main memory.

Function caching is a way to improve code's performance by storing the function's return values.

import functools

'''

import time
from functools import lru_cache

@lru_cache(maxsize=36)

def some_work(n):
    #the respective task taking up some time ie n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("now running the task ")
    some_work(2)
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(2)
    print("done---- calling now ")
    some_work(5)
    print("called again--executed ")