def CountNonFactors(iNo):
    iCnt = 0
    iFrequency = 0
    
    if(iNo < 0):
        iNo = - iNo
        
    for iCnt in range(1,iNo):
        if(iNo%iCnt != 0):
            iFrequency += 1
    return iFrequency
            
def main():
    iValue = 0
    iRet = 0
    
    iValue = int(input("Enter number : "))
        
    iRet = CountNonFactors(iValue)  
    
    print("Number of Non factors are : ",iRet)  
    
if __name__ == "__main__":
    main()