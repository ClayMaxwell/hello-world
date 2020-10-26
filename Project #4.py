HeightD = float(input("How high was the ball dropped from: "))
BouncinessI = float(input("How bouncy is the ball "))
Bounces = int(input("How many times did the ball bounce "))
Distance = 0
Height = HeightD * BouncinessI
Distance = Distance + HeightD
Distance = Height + Distance
Bounces = 1
print("The ball travelled ", Distance, "feet.")
