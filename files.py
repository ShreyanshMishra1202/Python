file1=open('my_files.txt','w')          # if any file with that name doesn't exist, it creates one
my_reading=file1.write("Hello Everyone")
print(my_reading)
file1.close()

file1=open('my_files.txt','r')
my_reading=file1.read()
print(my_reading)
file1.close()

file1=open('my_files.txt','a')
my_reading=file1.write("My Name is Shreyansh Mishra")
print(my_reading)
file1.close()

file1=open('my_files.txt','r')
my_reading=file1.read()
print(my_reading)
file1.close()


# -----------------------------------------------------------

file1=open('my_files.txt','r+')
f1=file1.write('My Name is Anthony Gonsalves')
print(f1)
# f1=file1.read()
# print(f1)
file1.close()

file1=open('my_files.txt','r+')
# f1=file1.write('My Name is Anthony Gonsalves')
# print(f1)
f1=file1.read()
print(f1)
file1.close()