# There are 2 methods of opening and closing a file
#1
file1=open('my_files.txt','r')
# directory ---> specifies the location
# modes ---> what permissions given(r,w,a,r+,.....)
reading_file=file1.read()
print(reading_file)
file1.close()

#2
# with open('my_file.txt','w') as file1:
    # Statement (Dont use closing syntax)
