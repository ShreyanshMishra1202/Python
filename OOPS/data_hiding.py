class simple:

    def __init__(self):
        self.value1=1
        self.value2=2

    def _A1_(self):
        print('Apple')
    def _B1_(self):
        print('Ball')
s=simple()
print(s.value1)
s._A1_()
s._B1_()


print('---------------------------------------------------')
# adding double underscore(__) before any function and variable hides it.
# and to access it, you first print(dir(classvariable_name)) and then,choose and write what's given there
class rr:
    def __init__(self):
        self.__v1=2
        self.__v2=4
    def __A(self):
        print("AAM")
    def __B(self):
        print("BABU")

a=rr()
print(dir(a))
a._rr__A()
a._rr__B()
print(a._rr__v1)
print(a._rr__v2)