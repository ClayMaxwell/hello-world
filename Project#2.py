FileName = input("Enter the file name: ")
File = open(FileName, 'r')
NumbLine = 0
for line in File:
    NumbLine = NumbLine + 1
print("The file has",NumbLine,"lines.")
while True:
    linenumb = 0
    numb = int(input("Enter a line number [0 to quit]: "))
    if numb >=1 and numb <= NumbLine:
        File = open(FileName, 'r')
        for lines in File:
            linenumb = linenumb + 1
            if linenumb == numb:
                print(numb,":",lines)
    elif numb == 0:
        break
    else:
        if numb!= NumbLine:
            print("Enter a line number that is less than",NumbLine)
