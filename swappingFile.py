def swapFileData():
    name=input("Enter the name of the file that you want to acess ")
    file1=open(name)
    file2=open('sample2.txt')
    data_a=file1.read()
    data_b=file2.read()
    with open(file1, 'w') as a:
        a.write(data_b)
    with open(file2, 'w') as a:
        a.write(data_a)
swapFileData()
    