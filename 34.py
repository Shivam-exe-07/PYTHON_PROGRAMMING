def CountFactorsNonFactors(iNo):
    iCnt = 0
    iFrequency1 = 0
    iFrequency2 = 0
    
    if(iNo < 0):
        iNo = -iNo
        
    for iCnt in range(1,iNo):
        if(iNo%iCnt == 0):
            iFrequency1 += 1
        else:
            iFrequency2 += 1
            
    print("Number of factors are : ",iFrequency1)
    print("Number of non factors are : ",iFrequency2)
                
def main():
    iValue = 0
    
    iValue = int(input("Enter number : "))
        
    CountFactorsNonFactors(iValue)  
    
if __name__ == "__main__":
    main()