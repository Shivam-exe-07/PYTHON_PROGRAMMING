def CheckDivisible(iNo1,iNo2):
    if((iNo1%iNo2) == 0):
        return True
    else:
        return False

def main():
    iValue1 = 0
    iValue2 = 0
    bRet = False
    
    iValue1 = int(input("Enter first number : "))
    iValue2 = int(input("Enter second number : "))
    
    bRet = CheckDivisible(iValue1,iValue2)
    
    if(bRet == True):
        print("It is completely divisible")
        
    else:
        print("It is not divisible")    
    
if __name__ == "__main__":
    main()