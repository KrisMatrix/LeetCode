# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = []
        ptr = head
        while(1):
          if ptr == None:
            break
          if ptr.next == None:
            array.append(ptr.val)
            break
          array.append(ptr.val)
          ptr = ptr.next
        reverse = ListNode("", None)
        if len(array) > 0:
          reverse = ListNode(0,None)        
        ptr = reverse
        for i in reversed(range(len(array))):
          if i == 0:
            ptr.val = array[i]
          else:
            ptr.val = array[i]
            ptr.next = ListNode(0,None)
            ptr = ptr.next
        return reverse
