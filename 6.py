def AdditionTwoNumbers(iNo1, iNo2):
    iSum = 0
    iSum = iNo1 + iNo2
    return iSum

def main():
    iValue1 = 0
    iValue2 = 0
    iRet = 0

    iValue1 = int(input("Enter first number : "))   
    iValue2 = int(input("Enter second number : "))  

    iRet = AdditionTwoNumbers(iValue1, iValue2)     

    print("Addition is : ", iRet)

if __name__ == "__main__":
    main()