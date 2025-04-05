# re.match(pattern, string, flags)

import re
pattern="apple"
if re.match(pattern,'apple'):
    print('True')
else:
    print('False')

# findall(string,pattern,flags)
# it gives consecutive string characters of string present in pattern
string=re.findall('apple',pattern)
print(string)
string=re.findall('app',pattern)
print(string)
string=re.findall('xyz',pattern)
print(string)
string=re.findall('ale',pattern)
print(string)