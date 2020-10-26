numbers = []
print("enter key to stop")
while(True):
    numbr = input("enter a number :")
    if numbr:
            numbers.append(int(numbr))
    elif(numbr == ''):
            break
sum =0
for numbr in numbers:
    sum += numbr
average = sum / len(numbers)
print("The sum is", sum)
print("The average is", average)
