def swapFileContent(file1, file2) : 
    f1 = open(file1)
    f2 = open(file2)

    f1text = f1.read()
    f2text = f2.read()

    f1 = open(file1, 'w')
    f2 = open(file2, 'w')

    f1.write(f2text)
    f2.write(f1text)

    f1 = open(file1, 'r')
    f2 = open(file2, 'r')

    f1text = f1.read()
    f2text = f2.read()    

    print(f1text)
    print(f2text)

    print('Swap Successful!')

fileone = input('Enter file 1:')
filetwo = input('Enter file 2:')

fileone1 = open(fileone, 'r')
filetwo2 = open(filetwo, 'r')

fileone11 = fileone1.read()
filetwo22 = filetwo2.read()

print(fileone11)
print(filetwo22)

swapFileContent(fileone, filetwo)