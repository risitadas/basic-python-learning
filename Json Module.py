'''
Json Module

JSON is already built-in in Python, so no need for an installation command.
We can import it so we may start working on it.
JSON module in Python helps us in converting the data structures to JSON strings.

import json

Methods:

load(): This method is used to load data from a JSON file into a python dictionary.
Loads( ): This method is used to load data from a JSON variable into a python dictionary.
dump(): This method is used to load data from the python dictionary to the JSON file.
dumps(): This method is used to load data from the python dictionary to the JSON variable.

Parsing :
it converts the code from one form to another,
making it compatible with running on the other platform by changing all the little syntax differences
and making it perfect for running on the other platform. The following table shows how Python objects
are converted to JSON objects.

JSON	PYTHON
true     true
false    false
string   string
number	 number
array    list, tuple
object 	 dict
null     none



'''

import json

data = '{"var1":"taylor","var2":"swift","var3":"13"}'
print(data)

parsed = json.loads(data)       # The json. load() is used to read the JSON document from file
                                # json.loads() is used to convert the JSON String document into the Python dictionary
print(data)
print(parsed['var2'])

# json.dumps() is actually used to convert any python object into a string in JSON
# and it also its own attributes like "indent" and "sort_keys"
# The value of the sort_keys argument of the dumps() function will require to set True to generate the sorted JSON objects from the array of JSON objects.

data2 = {
    "debut":"taylor swift",
    "2nd album":"fearless",
    "last album":"red taylor's version",
    "last song":"carolina",
    "any grammy album":('folklore',2021),
    "no of award nominations":"over 500"

}

jscomp = json.dumps(data2)
print(jscomp)