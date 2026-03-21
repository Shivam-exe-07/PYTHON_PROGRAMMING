def CountCapital(Brr):
    iCount = 0
    
    for ch in Brr:
        if(ch >= 65 and ch <= 91):      #issue
            iCount = iCount + 1
            
    return iCount

def main():
    print("Enter String : ")
    Arr = input()
     
    Ret = CountCapital(Arr)
    print("Number of Capital characters are : ",Ret)
                 
main()