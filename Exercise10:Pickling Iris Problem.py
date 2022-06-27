'''

Pickling Iris

Problem Statement:
The task you have to perform is “Pickling Iris.”
For this, Check the UC Irvine Machine Learning Repository site to get the dataset.
You can search the Iris dataset through their searchable interface. Follow the following steps to download the dataset:

i) Go to https://archive.ics.uci.edu/ml/index.php
ii) On Most Popular Data Sets, you will see the name “Iris.”
iii) Open the Iris dataset.
iv) Click on the Data folder. A new tab will open, which contains some files.
v) Click on the Iris. data file to download the text file.

After saving Iris data file, parse it using the split() function or using a new line approach.
The method of parsing is up to you.

The main task is to get the list of lists that you will pickle.
And after creating the pickle, write a code to read it.
For downloading the Iris dataset, use the request module.


'''



import requests
import pickle

data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
# print(data)

# l1 = data.split("\n")
# print(l1)

l2 =[item.split(",") for item in data.split("\n") if len(item)!=0]
# print(l2)

with open("myiris.pkl", "wb") as f:
    pickle.dump(l2, f)


# To read this pickle file we can use this code
# import pickle
# with open("myiris.pkl", "rb") as f:
#     print(pickle.load(f))
