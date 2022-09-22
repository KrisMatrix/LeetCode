from typing import Optional
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    list3 = ListNode(None,None)
    #print(list3.val)
    #print(type(list3.val))
    while(1):
      if list1.val == None:
        pass
      if list2.val == None:
        pass
      
      


obj = Solution()
obj.mergeTwoLists([1,2,4],[1,3,4])
obj.mergeTwoLists([],[])
obj.mergeTwoLists([],[0])
