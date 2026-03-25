def main():
    iValue1 = 0
    iValue2 = 0
    
    iValue1 = int(input("Enter first number : "))
    iValue2 = int(input("Enter second number : "))
    
    if((iValue1%iValue2) == 0):
        print("It is completely divisible")
        
    else:
        print("It is not divisible")    
    
if __name__ == "__main__":
    main()