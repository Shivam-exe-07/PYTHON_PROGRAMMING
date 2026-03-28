def CheckPrime(iNo):
    iCnt = 0
    iFrequency = 0
    
    if(iNo < 0):
        iNo = -iNo
        
    for iCnt in range(2,(iNo//2)+1):
        if(iNo%iCnt == 0):
            iFrequency += 1
            
    if(iFrequency==0):
        return True
    else:
        return False
                
def main():
    iValue = 0
    bRet = False
    
    iValue = int(input("Enter number : "))
        
    bRet = CheckPrime(iValue)
    
    if(bRet == True):
        print(iValue,"is prime number")
    else:
        print(iValue,"is not a prime number")
    
if __name__ == "__main__":
    main()