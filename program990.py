#   Singly Linear Linked List in Python (OOP)

#   Done
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
class SinglyLL:
    #   Done
    def __init__(self):
        self.first = None
        self.iCount = 0
     
    #   Done   
    def InserFirst(self,no):
        newn = Node(no)
        
        #   LL is empty
        if self.first == None:
            self.first = newn
        #   It contains at least one node
        else:
            newn.next = self.first
            self.first = newn
            
        self.iCount = self.iCount + 1
    
    #   Done        
    def InsertLast(self,no):
        newn = Node(no)
        
        #   LL is empty
        if self.first == None:
            self.first = newn
        #   It contains at least one node
        else:
            temp = self.first
            
            while(temp.next != None):
                temp = temp.next
                
            temp.next = newn
            
        self.iCount = self.iCount + 1
    
    def InsertAtPos(self, no, pos):
        pass
    
    def DeleteFirst(self):
        pass
    
    def DeleteLast(self):
        pass
    
    def DeleteAtPos(self):
        pass
    
    #   Done
    def Display(self):
        temp = self.first
        
        while (temp != None):
            print("| ",temp.data," |->",end=" ")
            temp = temp.next
        
        print("None")
        
    #   Done
    def Count(self):
        return self.iCount

def main():
    sobj = SinglyLL()
    
    sobj.InserFirst(101)
    sobj.InserFirst(51)
    sobj.InserFirst(21)
    sobj.InserFirst(11)
    
    print("Elements of linked list are : ")
    sobj.Display()
    
    print("Number of elements of linked list are : ",sobj.Count())
    
    sobj.InsertLast(111)
    sobj.InsertLast(121)
    
    print("Elements of linked list are : ")
    sobj.Display()
    
    print("Number of elements of linked list are : ",sobj.Count())
    
if __name__ == "__main__":
    main()