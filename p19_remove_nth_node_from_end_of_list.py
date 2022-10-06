# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Well we are told that there is at least one node
        # We are also guaranteed that n will be a number between 1 and size of ll.
        array = []                      #O(n) space 
        node = head 
        while (node != None):           # O(n) time and single pass
            array.append(node)
            node = node.next
        if n > len(array):
            return None
        if (len(array) - n-1) < 0:
            head = array[-n].next
            return head
        
        prev = array[-n-1]
        if array[-n].next == None:
            prev.next = None
        else:
            prev.next = array[-n + 1]
        return head
