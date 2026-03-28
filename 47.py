#program82.java
class Number:
    def CheckPerfect(self,iNo):
        i = 0
        iSum = 0
        
        if(iNo < 0):
            iNo = -iNo
        
        for i in range(1,(iNo//2)+1):
            if (iNo%i) == 0:
                iSum = iSum + i
                
        return (iSum == iNo)

def main():
    iValue = 0
    bRet = False
    
    iValue = int(input("Enter number : "))
    
    nobj = Number()
    bRet = nobj.CheckPerfect(iValue)    
    
    if(bRet == True):
        print(iValue, "is perfect number")
    else:
        print(iValue, "is not a perfect number") 
        
    nobj = None                                       

if __name__ == "__main__":
    main()
    
    
#BufferedReader bobj = new BufferedReader(...) --> not needed in python
#Integer.parseInt(bobj.readLine()) --> int(input(...))
#Scanner sobj = new Scanner(System.in) --> not needed