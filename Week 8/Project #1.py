import math
tolerance = 0.000001
def newton(a):
   estimate = 1.0
   while True:
        estimate = (estimate + a / estimate) / 2
        difference = abs(a - estimate ** 2)
        if difference <= tolerance:
            break
   return estimate
def main():
   while True:
       a = input("Enter a positive number or press enter to quit: ")
       if a == "":
           break
       a = float(a)
       print("The estimate is", newton(a))
if __name__ == "__main__":
    main()
