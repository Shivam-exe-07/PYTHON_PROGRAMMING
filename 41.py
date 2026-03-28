def SumDigits(iNo):
    iSum = 0
    iDigit = 0
    
    while(iNo != 0):
        iDigit = iNo % 10
        iNo = iNo//10
        iSum = iSum + iDigit
        
    return iSum

def main():
    iValue = 0
    iRet = 0
    
    iValue = int(input("Enter number : "))
    
    iRet = SumDigits(iValue)
    print("Sum of digits are : ",iRet)                                                

if __name__ == "__main__":
    main()