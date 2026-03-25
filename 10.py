def CheckEvenOdd(iNo):
    return((iNo % 2) == 0)

def main():
    iValue = 0
    bRet = False
    
    iValue = int(input("Enter number : "))
    
    bRet = CheckEvenOdd(iValue)
    
    if(bRet==True):
        print(iValue,"is Even number")
    
    else:
        print(iValue,"is odd number")
    
    
if __name__ == "__main__":
    main()