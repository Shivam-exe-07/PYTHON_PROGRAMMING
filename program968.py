def CountCapital(Brr):
    iCount = 0
    
    for i in range(len(Brr)):
        if(Brr[i] >= 65 and Brr[i] <= 91):      #issue
            iCount = iCount + 1
            
    return iCount

def main():
    print("Enter String : ")
    Arr = input()
     
    Ret = CountCapital(Arr)
    print("Number of Capital characters are : ",Ret)
                 
main()