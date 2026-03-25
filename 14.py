def Display(iFrequency):
        iCnt = 0
        
        if(iFrequency<0):
            print("Invalid Input")
            return
        
        for iCnt in range(1,iFrequency + 1):
            print("Jay Ganesh")    

def main():
    iCount = 0
    
    iCount = int(input("Enter the frequency : "))
    
    Display(iCount)
    
if __name__ == "__main__":
    main()