def CheckEvenOdd(iNo):
    iRem = 0
    
    iRem = iNo % 2
    
    if(iRem == 0):
        print("it is even number")
        
    else:
        print("it is odd number")

def main():
    iValue = 0
    
    iValue = int(input("Enter number : "))
    
    CheckEvenOdd(iValue)
    
if __name__ == "__main__":
    main()