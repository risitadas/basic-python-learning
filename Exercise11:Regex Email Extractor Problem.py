'''

Regex Email Extractor

Problem Statement:-

The task you have to perform is "Email Extractor."
Suppose you are a student and want to get an internship.
You have to contact your professors and some companies to get an internship.
For that, you need their email so that you can contact them.
The task you have to do is to extract the email from text data using Regex Expressions.
When you go to a website and click on the contact section, by pressing CTRL+A,
all the website's content gets added to the clipboard. Paste the data in your python file or in a string.
Extract an email from the above data, and after extracting the email,
write it into a file with a new line character.
Your text file after writing data should look similar to this:

    abc123@gmail.com

    cdf456@gmail.com


'''

import re

text = "please contact us at snlsemiconductors13@gmail.com for furthur details. "+\
    "you can also give us your reviews and feedback at feedpcs@sns.com"

emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
print(emails)
