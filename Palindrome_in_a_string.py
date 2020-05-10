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
            temp = temp.next
        
    def palindromcheck(self):
        temp = self.head
        stack = []
        while temp:
            stack.append(temp.data)
            temp = temp.next
        
        temp = self.head
        while temp:
            stack_element = stack.pop()
            ll_element = temp.data
            if stack_element == ll_element:
                temp = temp.next
            else:
                return "Not a palindrome"
        if len(stack) ==0:
            return "It is a palindrome"
        
        
l = LL()
l.head = Node(4)
second = Node(1)
third = Node(3)
four = Node(3)
five = Node(1)
six = Node(4)

l.head.next = second
second.next = third
third.next = four
four.next = five
five.next = six
l.printlist()
val = l.palindromcheck()
print(val)

