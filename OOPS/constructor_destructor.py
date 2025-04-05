class const_dest:
    x=0

    def __init__(self,color,type):
        self.color=color
        self.type=type
        print("Constructed")
    def __del__(self):
        print("Destructed")

a=const_dest("Black","SUV")
print(a.color)
print(a.type)

a1=const_dest("Red","Sedan")
print(a1.color)
print(a1.type)
