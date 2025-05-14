try:
    with open('sample.txt','r') as file:
        f1=file.read()
        print(f1)
except:
    print("Error: The file 'sample.txt' was not found." )
