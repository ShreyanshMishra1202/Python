class name:
    x=0
    name=""

    def __init__(self,z):
        self.name=z
        print("Hi",z)

class football_fans(name):          # By using this name in parenthesis, we inherit features from other class
    points=0

    def pts(self):
        print(self.name,"scores")

m=name("Jim")
n=football_fans("Sam")
n.pts()