# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:                 #check if both are not empty. i.e. if both empty, it wouldn't execute the rest.
            if list1.val > list2.val:
                list1, list2 = list2, list1 # We are basically combining list1 and list 2. list1 will eventually become the 
                                            # merge sorted list
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1 or list2
