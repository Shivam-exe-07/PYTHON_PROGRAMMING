#program90.java
class Digit:
    def DisplayDigits(self,iNo):
        iDigit = 0
        
        while(iNo != 0):
            iDigit = iNo%10
            print(iDigit)
            iNo = iNo//10

def main():
    iValue = 0
    
    iValue = int(input("Enter number : "))
    
    dobj = Digit()
    dobj.DisplayDigits(iValue)    
        
    dobj = None                                       

if __name__ == "__main__":
    main()
    
    
#BufferedReader bobj = new BufferedReader(...) --> not needed in python
#Integer.parseInt(bobj.readLine()) --> int(input(...))
#Scanner sobj = new Scanner(System.in) --> not needed