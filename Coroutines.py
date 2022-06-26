'''

Coroutines in Python

Coroutines are mostly used in cases of time-consuming programs,
such as tasks related to machine learning or deep learning algorithms,
or in cases where the program has to read a file containing a large number of data.

We can define a coroutine using the following statements.

def myfunc():
    while True:
        value = (yield)

Coroutine Execution:-
Execution is the same as of a generator.
They only run in response to the next() and send() methods.

When we run the next() function the first time, the coroutine executes and waits for new input.
After the input is sent to it using the send() function, it executes it and again waits for next input,
and the process goes on like this because we have set the while loop as true, so it will never exit its execution.
In order to make the execution stop, we have to close the coroutine using coroutine.close() function.

send() — used to send data to coroutine
close() — to close the coroutine


'''


def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is where all the madness starts with the girl staring out of the window "
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search)
print("Next method run")
search.send("boy")

search.close()
search.send("girl")




