class Node: 
  
    def __init__(self, data): 
        self.data = data 
        self.next = None  

class LinkedList: 
   
    def __init__(self): 
        self.head = None
  
    def printList(self): 
        temp = self.head 
        while (temp): 
            print (temp.data) 
            temp = temp.next
  
if __name__=='__main__': 

    List1 = LinkedList() 
    List1.head = Node(4) 
    second = Node(2) 
    third = Node(5) 
  
    List1.head.next = second; 
    second.next = third; 
  
    List1.printList() 