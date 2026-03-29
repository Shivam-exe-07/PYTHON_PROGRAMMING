#program91.java
class Digit:
    def SumDigits(self,iNo):
        iDigit = 0
        iSum = 0
        
        while(iNo != 0):
            iDigit = iNo%10
            iSum = iSum + iDigit
            iNo = iNo//10
            
        return iSum

def main():
    iValue = 0
    iRet = 0
    
    iValue = int(input("Enter number : "))
    
    dobj = Digit()
    iRet = dobj.DisplayDigits(iValue)    
    
    print("Addition of digits : ",iRet)
        
    dobj = None                                   

if __name__ == "__main__":
    main()
    
    
#BufferedReader bobj = new BufferedReader(...) --> not needed in python
#Integer.parseInt(bobj.readLine()) --> int(input(...))
#Scanner sobj = new Scanner(System.in) --> not needed