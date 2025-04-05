name='Mike'
number=len(name)*3
print("Hello {},your lucky number is {}.".format(name,number))

example="format() method"
string="This is an example of {} on a string.".format(example)
print(string)

a='apple'
b='ball'
c=45
print("{} {} {}".format(a,b,c))
print("{0} {2} {1}".format(a,b,c))      # it prints index wise as given in format parenthesis


price=150
with_tax=150+45
print("Price ={:.2f} and with tax ={:.2f}".format(price,with_tax))