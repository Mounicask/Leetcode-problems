class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LL():
    def __init__(self):
        self.head = None
        
    def printlist(self):
        temp = self.head
        
        while temp:
            print(temp.data)
            temp = temp.next
        
    def reverselist(self):
        reversed_node = self.head
        list_to_do = self.head.next
        reversed_node.next = None
        temp = None
        while list_to_do!= None:
            temp = list_to_do 
            list_to_do = list_to_do.next
            temp.next = reversed_node
            reversed_node = temp
        self.head = temp
                
l = LL()
l.head = Node(1)
second = Node(2)
third = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

l.head.next = second
second.next = third
third.next = four
four.next = five
five.next = six

l.printlist()
l.reverselist()
print("After reverse ***")
l.printlist()
