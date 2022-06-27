'''

Regular Expression Task

Given a string with a lot of indian phone numbers starting from +91,
return a list that contains all of them

'''

import re

mystr = '''

Tata Limited
Dr. David Landsman, executive director
Fax: +91 (20) 7335 8727
Fax: +91 (20) 7235 8727
Phone: +91 (20) 7235 8281
Fax: +91 (20) 7235 8727
Fax: +91 (20) 7295 8727
Fax: +91 (20) 7235 8027
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Fax: +91 (20) 9235 8727
Phone: +91 (703) 243 9787
Fax: +91 (703) 243 9791
Fax: +91 (20) 7235 8975
Fax: +91 (20) 8935 8727
Fax: +91 (20) 7235 8765
Fax: +91 (20) 7235 8700

'''


patt=re.compile(r'[+91]\d+')

matches=patt.finditer(mystr)
for match in matches:
    print(match)

