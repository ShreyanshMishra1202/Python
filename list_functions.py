a=[1,2,3,4,5,6,7,8]
a.append(12)        # adds only one elements to list
print(a)
a.extend([10,44])       # adds many elements to the list
print(a)

a.remove(10)
print(a)
del a[0]
print(a)
del a[0:2]
print(a)
del a
# print(a)    cannot be done as del a deletes the list from memory location
d=[1,2,3,4]
d.clear()
print(d)