def CheckEven(No):
    if(No%2 == 0):
        print("It is even number")
    else:
        print("It is odd number")


def main():
    Value = 0
    
    print("Enter Number : ")
    Value = int(input())
    
    CheckEven(Value)

main()