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
    
    print("Result is : ",bRet)
    
if __name__ == "__main__":
    main()