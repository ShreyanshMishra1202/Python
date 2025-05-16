details={'Harry':70,'Alice':85,'Virat':90}
a=input("Enter the student's name: ")
if a in details:
    print(a+"'s marks:",details[a])
else:
    print("Student not found")