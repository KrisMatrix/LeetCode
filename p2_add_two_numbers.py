# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l3 = ListNode(None,None)
    ptr_l1 = l1
    ptr_l2 = l2
    ptr_l3 = l3
    carry = 0
    # Assuming l1 and l2 are same length, we can step through both of them 
    # one step at a time.
    # but if l1 and l2 are of different lengths, then we can stop stepping 
    # through the short LL when we reach the end.
    # We are told that the LL will always have SOME content. So at least
    # a length of 1.
    while (1):
      ptr_l3.val = ptr_l1.val + ptr_l2.val + carry
      carry = 0 #reset the carry
      if ptr_l3.val >= 10:
        carry = ptr_l3.val // 10;
        ptr_l3.val = ptr_l3.val % 10
      
      if ptr_l1.next == None and ptr_l2.next == None:
        if carry:
          ptr_l3.next = ListNode(carry, None)
        break 
        
      if ptr_l1.next != None:
        ptr_l1 = ptr_l1.next
      else:
        ptr_l1.val = 0
      
      if ptr_l2.next != None:
        ptr_l2 = ptr_l2.next
      else:
        ptr_l2.val = 0
        
      ptr_l3.next = ListNode(0,None)
      ptr_l3 = ptr_l3.next     
    return l3
