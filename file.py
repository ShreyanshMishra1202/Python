# There are 2 methods of opening and closing a file
#1
'''
file1=open('my_files.txt','r')
# directory ---> specifies the location
# modes ---> what permissions given(r,w,a,r+,.....)
f1=file1.read()             # reads whole file
f2=file1.read(5)            # reads only x no. of character given in parenthesis() of read
f3=file1.readline()         # reads a single line
f4=file1.readlines()        # reads all lines but creates list of every lines
print(f1)
print(f2)
print(f3)
print(f4)
file1.close()
'''

#2
with open('my_files.txt','r') as file1:
    # Statement (Dont use closing syntax)
    f1=file1.read()     # we can apply other functions too as of 1st method
    print(f1)
