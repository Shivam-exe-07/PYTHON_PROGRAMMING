def DisplayFactors(iNo):
    iCnt = 0
    
    if(iNo < 0):
        iNo = - iNo
        
    for iCnt in range(1,iNo):
        if(iNo%iCnt == 0):
            print(iCnt)
            
def main():
    iValue = 0
    
    iValue = int(input("Enter number : "))
    
    DisplayFactors(iValue)    
    
if __name__ == "__main__":
    main()