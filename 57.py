#program94.java
class ArrayX:
    def Display(self,Brr):
        i = 0
        
        for i in range(0,len(Brr)):
            print(Brr[i])

def main():
    Arr = [10,20,30,40]
    
    aobj = ArrayX()      
    
    aobj.Display(Arr)    

if __name__ == "__main__":
    main()
    
    
#BufferedReader bobj = new BufferedReader(...) --> not needed in python
#Integer.parseInt(bobj.readLine()) --> int(input(...))
#Scanner sobj = new Scanner(System.in) --> not needed