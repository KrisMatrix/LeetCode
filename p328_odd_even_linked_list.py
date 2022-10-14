# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = None
        stack_ptr = stack
        odd_node = head
        if head == None:
            return head
        while(odd_node.next != None):
            even_node = odd_node.next
            if (even_node.next == None):
                if stack == None:
                    stack = even_node
                    stack_ptr = stack
                else:
                    stack_ptr.next = even_node
                    stack_ptr = stack_ptr.next
                    stack_ptr.next = None
                break
            odd_node.next = even_node.next
            even_node.next = None
            if stack == None:
                stack = even_node
                stack_ptr = stack
            else:
                stack_ptr.next = even_node
                stack_ptr = stack_ptr.next
                stack_ptr.next = None
            odd_node = odd_node.next
        
        odd_node.next = stack
        return head
