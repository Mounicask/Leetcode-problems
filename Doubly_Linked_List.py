class Node():
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
        
class DoublyLL():
    def __init__(self):
        self.head = None
        
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def insertBegin(self,data):
        temp = self.head
        
        insert_node = Node(data)
        insert_node.prev = None
        insert_node.next = temp
        
        self.head = insert_node
        temp.prev = insert_node
      
    def insertLast(self,data):
        temp = self.head
        while temp.next:
            temp = temp.next
        
        insert_node = Node(data)
        insert_node.prev = temp
        insert_node.next = None
        
        temp.next = insert_node
        
l = DoublyLL()
l.head = Node(1)
second = Node(2)
third = Node(3)
l.head.prev = None
l.head.next = second
second.prev= l.head
second.next = third
third.prev = second
third.next = None
l.printlist()
print("**************")
l.insertBegin(9)
l.printlist()
print("**************")
l.insertLast(100)
l.printlist()
print("**************")
l.insertBegin(8)
l.printlist()
print("**************")
l.insertLast(2---00)
l.printlist()