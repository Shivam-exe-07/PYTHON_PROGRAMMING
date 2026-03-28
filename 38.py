def main():
    iNo = 723614
    iDigit = 0

    print("-------------------------------------------")
    print("Original value of iNo is :", iNo)

    while (iNo != 0):
        print("-------------------------------------------")
        iDigit = iNo % 10
        print("iDigit is :", iDigit)
        iNo = iNo // 10
        print("iNo is :", iNo)

    print("-------------------------------------------")  
    print()                                                

if __name__ == "__main__":
    main()