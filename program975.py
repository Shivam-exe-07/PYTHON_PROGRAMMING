def ToggleCase(Brr):
    Result = ""
    
    for ch in Brr:
        if(ch >= 'A' and ch <= 'Z'):
            Result = Result + chr(ord(ch) + 32)
        elif(ch >= 'a' and ch <= 'z'):
            Result = Result + chr(ord(ch) - 32)
        else:
            Result = Result + ch
            
    return Result

def main():
    print("Enter String : ")
    Arr = input()
    
    Ret = ToggleCase(Arr)
    
    print("Updated String is : ",Ret)
                 
main()