from fontTools.misc.cython import returns


def add(i,j):
    return i+j
res=add(1,2)
print(res)
a=add
res1=a(1,4)
print(res1)
def call(i,j):
    return add(i,j)
print(call(2,4))
def pas(i,j,fn):            # we pass here name of function(eg- call,add,etc) to fn
    return fn(i,j)
print(pas(1,3,call))