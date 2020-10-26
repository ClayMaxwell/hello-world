inputFileName = input("Enter the filename: ")
userfile = open(inputFileName, 'r')
outputFileName = input("Enter the output filename: ")

inputFile = open(inputFileName, 'r')  
outputFile = open(outputFileName, 'w')  

count = 1  
for line in inputFile:
    text = str(count).rjust(4, " ") + "> " + line
    outputFile.write(text) 
    print(text)
    count += 1

inputFile.close()
outputFile.close()
