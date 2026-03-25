def Display(iNo):
        iCnt = 0
        
        for iCnt in range(iNo,0,-1):
            print(iCnt,end = "\t")
        print()  

def main():
    iValue = 0
    iValue = int(input("Please Enter frequency : "))
    Display(iValue)
    
if __name__ == "__main__":
    main()