'''
#  Normal Program
x=[]
for i in range(11):
    if i**2 %2=0:
        z=i**2
        x.append(z)
print(x)
'''


# List Comprehension Syntax
# [expression for items in list {if (test expression)}]
x=[i**2 for i in range(11) if i**2 %2==0]
print(x)