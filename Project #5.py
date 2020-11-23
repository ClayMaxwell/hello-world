def isSorted(number):
     if len(number) >= 0 and len(number) < 2:
          return True
     else:
          if len(number) < 0 and len(number) > 2:
               return False
def main():
     number = [23]
     print(isSorted(number))
     number = [14]
     print(isSorted(number))   
     number = [-88]   
     print(isSorted(number))
     number = [6]  
     print(isSorted(number))

main()
