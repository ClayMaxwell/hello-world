Organisms = int(input("How many organisms are there: "))
RateOfGrowth = int(input("What is the growth rate (a real number greater than 0): "))
NumberOfHours = int(input("How many hours are needed to achieve growth rate: "))
TotalHours = int(input("How many hours of growth were there: "))
Hours=0
while (Hours <= TotalHours):
    Organisms*=RateOfGrowth
    Hours += NumberOfHours
    if (Hours==TotalHours):
        break
print("The total organism population is",Organisms)
