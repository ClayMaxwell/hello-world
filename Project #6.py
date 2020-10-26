X = int(input("Enter the value for X:"))
Value = 0
for y in range(1,X):
    Value += (-1)**(y+1)*((1.0/(y+y+1)))
Val = 4 * (1 - Value)
print(Val)
