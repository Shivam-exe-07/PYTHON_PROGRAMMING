#program75.java
def main():
    iNo = 0
    i = 0
    
    iNo = int(input("Enter number : "))
    
    for i in range(1,(iNo//2)+1):
        if((iNo%i)==0):
            print(i)                                             

if __name__ == "__main__":
    main()
    
    
#BufferedReader bobj = new BufferedReader(...) --> not needed in python
#Integer.parseInt(bobj.readLine()) --> int(input(...))