def Display(iNo):
        iCnt = 0
        
        for iCnt in range(1,iNo+1):
            print(iCnt,end = "\t")
            iCnt += 1
        print()  

def main():
    Display(7)
    
if __name__ == "__main__":
    main()