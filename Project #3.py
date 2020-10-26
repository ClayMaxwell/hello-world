import math
Lower = int(input("Enter lowest possible number: "))
Higher = int(input("Enter the highest possible number: "))
maxguess = math.ceil(math.log(Higher - Lower))
count = 0
guess = int((Lower + Higher) / 2)
while count != maxguess:
    count += 1
    guess = int((Lower + Higher) / 2)
    print(Lower, Higher)
    print("Your number is: ", guess)
    hint = input("Enter Correct, Lower, or Higher: ")
    if hint == 'Higher':
        Lower = guess + 1
    elif hint == 'Lower':
        Higher = guess - 1
    elif hint == 'Correct':
        print("The computer guessed your number in", count, "guesses")
        break
else:
    print("I'm out of guesses, and you cheated")
