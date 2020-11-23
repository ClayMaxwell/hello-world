def main():
    filename = input("Please enter your filename:")
    file = open(filename, "r")
    
    f = file.read().split()

    number = []
    for line in f:
        number.append(int(line))
    file.close()
    
    average = float(sum(number))/len(number)
    print("Your average is",average)
main()
