class A:

    def state1(self):
        print("State 1 present.")
    def state2(self):
        print("State 2 present.")
    def state3(self):
        print("State 3 present.")

class B:

    def state4(self):
        print("State 4 present.")
    def state5(self):
        print("State 5 present.")

class C(A,B):           # class C inherits functions of class A and B as they are called

    def state6(self):
        print("State 6 present")

a=A()
a.state1()

b=B()
b.state5()

c=C()
c.state1()
c.state5()
c.state6()