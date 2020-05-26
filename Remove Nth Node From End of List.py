# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        temp = head
        temp1 = dummy
        count= 0
        while temp:
            count = count + 1
            temp = temp.next
        if count == 1:
            return None
        till = count - n
        while till:
            till = till - 1
            temp1 = temp1.next
        temp1.next = temp1.next.next 
        return dummy.next