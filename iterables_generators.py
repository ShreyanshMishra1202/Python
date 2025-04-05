# ITERATOR

list=[1,2,3,4,5]
iteration = iter(list)
print(iteration.__next__())
print(iteration.__next__())
print(next(iteration))
print(next(iteration))

print('--------------------------------------------------------------')

# GENERATORS   --  these create iterators
def fn():
    yield 1
    yield 2
    yield 3

values=fn()
# for i in values:
#     print(i)
# you may use this for loop or values.__next__ to go through the data in generator
print(values)
print(values.__next__())
print(values.__next__())
print(values.__iter__())        # it gets you the generator

print('-------------------------------------------------------------------')

def square():
    n=1
    while(n<=5):
        square=n**2
        yield square
        n+=1

values1=square()
for i in values1:
    print(i)