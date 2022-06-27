'''

Pickle Module

Pickling :-
its the process of serializing an object.
Serializing means storing the object in the form of binary representation so it can be saved in our main memory.
The object could be of any type. It could be a string, tuple, or any other sort of object that Python supports.

To use pickle, we have to import it in Python.

import pickle

for example :

py_dict = { 'name': 'risita', 'salary':1300, 'language': 'english' }
myfile = open('filename','wb')
pickle.dump(py_dict,myfile)
myfile.close()


Unpickling :-
The file format is binary, so we cannot directly open and read it;
instead, we have to open it using a python program, and the process is known as unpickling.
We have to open the file in "rb" mode for unpickling, also known as a read binary mode.
The function we use this time is also a built-in function, named load().

for example :

myfile = open(filename,'rb')
py_dict = pickle.load(myfile)
myfile.close()


some of the common pickle exceptions raised while dealing with the pickle module. are as follows :-

i) Pickle.PicklingError: If the pickle object does not support pickling, then Pickle.PicklingError exception is raised.
ii) Pickle.UnpicklingError: This exception will raise if the file contains bad or corrupted data.
iii) EOF Error: This exception will be raised if the end of the file is detected.


'''

import pickle

# pickling a python object

#artists = ["Taylor Swift", "Conan Gray", "Cigarettes after sex"," Private island", "the 1975", "orion sun", "jack harlow"]
#file = "artists.txt"
#fileobj = open(file,'wb')
#pickle.dump(artists, fileobj)
#fileobj.close()


# unpickling a python object

file = "artists.pkl"
fileobj = open(file, 'rb')
artists = pickle.load(fileobj)
print(artists)
print(type(artists))


#pickle.load() - takes file object and return corresponding python format (readable )
#pickle.loads() - takes the binary format and returns python format
#pickle.dumps() - takes the variable and returns binary string