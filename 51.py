#program86.java
class Number:
    def CalculateFactorial(self,iNo):
        i = 0
        iFact = 0
        
        for i in range(1, iNo):
            iFact =iFact * i    
            
        return iFact

def main():
    iValue = 0
    iRet = 0
    
    iValue = int(input("Enter number : "))
    
    nobj = Number()
    iRet = nobj.CalculateFactorial(iValue)    
    
    print("Factorial is : " ,iRet) 
        
    nobj = None                                       

if __name__ == "__main__":
    main()
    
    
#BufferedReader bobj = new BufferedReader(...) --> not needed in python
#Integer.parseInt(bobj.readLine()) --> int(input(...))
#Scanner sobj = new Scanner(System.in) --> not needed