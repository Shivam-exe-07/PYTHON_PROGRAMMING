#program99.java
class ArrayX:
    def Display(self,Brr):
        i = 0
        
        for i in range(0,len(Brr)):
            print(Brr[i])

def main():
    iSize = 0
    
    iSize = int(input("Enter the size of array : "))
    
    Arr = [None] * iSize
    
    print("Enter the elements:")

    Arr[0] = int(input())
    Arr[1] = int(input())
    Arr[2] = int(input())
    Arr[3] = int(input())
    Arr[4] = int(input())
    
    aobj = ArrayX()      
    aobj.Display(Arr)    

if __name__ == "__main__":
    main()
    
    
#BufferedReader bobj = new BufferedReader(...) --> not needed in python
#Integer.parseInt(bobj.readLine()) --> int(input(...))
#Scanner sobj = new Scanner(System.in) --> not needed