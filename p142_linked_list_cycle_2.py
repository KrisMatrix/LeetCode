# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return_node = None
        while head:
            return_node = head
            if head.next == None:
                return None
            if hasattr(head, 'flag'):
                return_node = head
                break
            else:
                head.flag = 1
                head = head.next
        return return_node
