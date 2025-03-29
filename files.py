file1=open('my_files.txt','w')          # if any file with that name doesn't exist, it creates one
my_reading=file1.write("Hello Everyone")
print(my_reading)
file1.close()

file1=open('my_files.txt','r')
my_reading=file1.read()
print(my_reading)
file1.close()