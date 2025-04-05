# syntax

# class (name):
#       statements & attributes
#       .....
#
# call the class
# statements

#1
class car:
    pass        # it passes the class
a=car()
print(a)

print('-------------------------------------------------')

#2
class car:
    color="black"
a=car()
print(a)
print(a.color)
print(a.__class__)

print('--------------------------------------------------')

#3
class car:
    color="black"
    type="SUV"
a=car()
print(a.color.upper())

print('---------------------------------------------------')

#4
class num:
    i=1
    j=2
def add(i,j):
    return i+j
a=num()
print(add(a.i,a.j))

print('----------------------------------------------------')

