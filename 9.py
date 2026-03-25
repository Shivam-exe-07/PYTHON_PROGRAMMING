def CheckEvenOdd(iNo):
    iRem = 0
    
    iRem = iNo % 2
    
    if(iRem == 0):
        return True
        
    else:
        return False

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