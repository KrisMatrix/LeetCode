# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
      # Set a ptr. traverse the LL, store each node into array
      # return middle of node
      ptr = head
      array = []
      while(1):
        if ptr.next == None:
          array.append(ptr)
          break
        array.append(ptr)
        if ptr.next != None:
          ptr = ptr.next
      
      if len(array) % 2 == 0:
        return array[ int(len(array)/2)]
      else:
        return array[int(floor(len(array)/2))]
