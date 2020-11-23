import math

tolerance = 0.000001
def newton(a, estimate = 1.0):
        difference = abs(a - estimate ** 2)
        if difference <= tolerance:
           return estimate
        else:
            return newton(a, (estimate + a / estimate) / 2)
def main():
   while True:
       a = input("Enter positive number or press enter to quit: ")
       if a == "":
           break
       a = float(a)
       print("The estimate is", newton(a))
if __name__ == "__main__":
    main()
