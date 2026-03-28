#program78.java
class Number:
    def DisplayFactors(self,iNo):
        i = 0
        
        for i in range(1,(iNo//2)+1):
            if (iNo%i) == 0:
                print(i)

def main():
    iValue = 0
    
    iValue = int(input("Enter number : "))
    
    nobj = Number()
    nobj.DisplayFactors(iValue)                                            

if __name__ == "__main__":
    main()
    
    
#BufferedReader bobj = new BufferedReader(...) --> not needed in python
#Integer.parseInt(bobj.readLine()) --> int(input(...))
#Scanner sobj = new Scanner(System.in) --> not needed