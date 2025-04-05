# Filter
# Syntax
# filter (functions, iterable)
# for displaying, convert filter to list/tuple/set
def even(a):
    return a%2==0
num=[1,2,3,4,5,6,7]
res=list(filter(even,num))
print(res)

res1=list(filter(lambda a:a%2==0,range(11)))
print(res1)