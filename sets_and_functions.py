a={1,2,3,4,5,1,2}       # will remove last 1 and 2 as it contains only unique elements (unordered)
print(a)
a.add(11)
print(a)
a.remove(1)
print(a)
print(2 in a)
print(45 in a)
print(3 not in a)

set1={1,2,3,4,5}
set2={3,4,5,6,7}
print(set1.intersection(set2))          # we can also use print(set1 & set2)
print(set1.union(set2))
print({1,2,3}.issubset(set1))
print(set1.issuperset({1,2,3}))