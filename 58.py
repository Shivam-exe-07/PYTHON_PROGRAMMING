#program97.java
class ArrayX:
    def Display(self,Brr):
        i = 0
        
        for i in range(0,len(Brr)):
            print(Brr[i])

def main():
    Arr = [None] * 4
    
    Arr[0] = 10
    Arr[1] = 20
    Arr[2] = 30
    Arr[3] = 40
    
    aobj = ArrayX()      
    
    aobj.Display(Arr)    

if __name__ == "__main__":
    main()
    
    
#BufferedReader bobj = new BufferedReader(...) --> not needed in python
#Integer.parseInt(bobj.readLine()) --> int(input(...))
#Scanner sobj = new Scanner(System.in) --> not needed