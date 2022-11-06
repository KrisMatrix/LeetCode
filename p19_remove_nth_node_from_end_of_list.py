# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        array = []
        ptr = head
        while ptr != None:
            array.append(ptr)
            ptr = ptr.next
        if n == len(array):
            if len(array) > 1:
                head = array[1]
                return head
            else:
                return None
        array[len(array)-n-1].next = array[-n].next
        return head

        # For reference:
        #prev_node = array[len(array)-n-1]
        #next_node = array[-n].next
        #prev_node.next = next_node
