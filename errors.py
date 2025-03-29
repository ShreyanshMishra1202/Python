#Syntax Error
'''
n=0
if(n==3):
    print("Hello")
else                                    # here : sign is not there
    print("World")
'''

# Indentation Error
'''
n=0
if n==3:
    print("Hello")
else:
print("World")                         # Indentation missing here
'''

# ZeroDivision Error
'''
n=8
print(8/0)
'''

# ModuleNotFound Error
'''
import mathematics              # math is the right module to be imported (not mathematics)
print(mathematics.pi)
'''

# Type Error
'''
a=4
b='S'
print(a+b)          # int and string cannot be added
'''

# Logical Error
'''
a=4
b=6
print(a*b)          # Logical Errors are in mind. here,we were to add but mistakely, multiply is done
'''

a=0
b=9
print(a+b)