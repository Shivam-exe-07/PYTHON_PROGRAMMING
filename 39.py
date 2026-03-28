def CountDigits(iNo):
    iDigit = 0
    iCount = 0
    
    while(iNo != 0):
        iDigit = iNo % 10
        iNo = iNo//10
        iCount += 1
        
    print()
    return iCount

def main():
    iValue = 0
    iRet = 0
    
    iValue = int(input("Enter number : "))
    
    iRet = CountDigits(iValue)
    print("Number of digits are : ",iRet)                                                

if __name__ == "__main__":
    main()