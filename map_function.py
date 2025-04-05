# Map
# map(function,iterable)

def square(a):
    return a**2

num=[1,2,3,4,5]
ans=list(map(square,num))
print(ans)

ans1=list(filter(square,num))
print(ans1)