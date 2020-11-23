import math
def newton(a, estimate):
    if abs (a-estimate ** 2) <= 0.000001:
            return estimate
    else:
        estimate = newton(a, (estimate + a/estimate)/2)
    return estimate  

def main():
    while True:
        a = (input("Enter a positive number or press enter key to quit: "))
        if a == "":    
                break
        a = float(a)
        print("Newton estimate of the sqaure root is: ", newton(a, a/2))
main()
