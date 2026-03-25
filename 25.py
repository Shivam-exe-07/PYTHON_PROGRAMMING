def Display(iNo):
        iCnt = 0
        
        for iCnt in range(2,iNo+1,2):
            print(iCnt,end = "\t")
        print()  

def main():
    iValue = 0
    iValue = int(input("Please Enter frequency : "))
    Display(iValue)
    
if __name__ == "__main__":
    main()