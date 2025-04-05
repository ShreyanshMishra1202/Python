def name(name):
    print("Hi",name)
n=name("Jim")
n=name("Sam")

print("------------------------------------------------------")

class name:
    x=0
    name=""

    def __init__(self,z):
        self.name=z
        print("Hi",z)

n=name("Peter")
n=name("Nixon")
print(n.name)