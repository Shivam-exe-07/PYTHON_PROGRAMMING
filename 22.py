def Display(iNo):
        iCnt = 0
        
        for iCnt in range(1,iNo+1):
            print(iCnt,end = "\t")
            iCnt += 1
        print()  

def main():
    iValue = 0
    iValue = int(input("Please Enter frequency : "))
    Display(iValue)
    
if __name__ == "__main__":
    main()