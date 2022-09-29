# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash = {}
        ptr = head
        prev_node = None
        while(ptr != None):
            if ptr.val not in hash.keys():
                hash[ptr.val] = 1
                prev_node = ptr
                ptr = ptr.next
            else:
                prev_node.next = ptr.next
                ptr = ptr.next
        return head
