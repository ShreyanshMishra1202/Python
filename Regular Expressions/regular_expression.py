# regular expression
# regex
# mostly used for strings
# import re
# validate the input

#1 match()
import re
pattern="apple"
# re.match(pattern,string) will only checks in string only the no of characters present in pattern
if re.match(pattern,'apple'):
    print('True')
else:
    print('False')

if re.match(pattern,'appleball'):
    print('True')
else:
    print('False')

if re.match(pattern,'appapple'):
    print('True')
else:
    print('False')
