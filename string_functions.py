s1="tRipoLi"
print(s1.capitalize())
print(s1.upper())
print(s1.lower())

a='d'
print(a.isalpha())
b='7'
print(b.isnumeric())
z='Mike is a good man'
print(z.startswith('Mike'))
print(z.endswith('man'))
print(z.replace('Mike','Nick'))
print(z)
print(z.find('good'))


q='   Lion is brave   '
print(q.lstrip())
print(q.rstrip())
print(q.strip())
print(q.split())



w='A man\nwe are good'
print(w.split())
print(w.splitlines())

h='lion','tiger','peigon'       # it acts like a tuple
n='*'
print(n.join(h))