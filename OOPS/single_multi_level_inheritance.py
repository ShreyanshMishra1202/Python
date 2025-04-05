# TYPES OF INHERITANCE
# SINGLE-LEVEL
# MULTI-LEVEL
# MULTIPLE


# SINGLE-LEVEL INHERITANCE

class A:

    def state1(self):
        print("State 1 present.")
    def state2(self):
        print("State 2 present.")
    def state3(self):
        print("State 3 present.")

class B(A):         # class B will have all functions of A as it inherits A

    def state4(self):
        print("State 4 present.")
    def state5(self):
        print("State 5 present.")

a=A()
a.state1()
a.state2()

print('-----------------------------------------')

b=B()
b.state4()
b.state1()          # it can be caled from class B becoz inheritance is done of A into B
b.state3()
b.state5()

print('----------------------------------------------')

# MULTI-LEVEL INHERITANCE
class C(B):             # class C will have all functions of (B and A) as C inherits B and B inherits A

    def state6(self):
        print("State 6 present")

c=C()
c.state1()
c.state5()
c.state6()

print('---------------------------------------------')

