# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array = []  # O(n) space complexity
        while(head != None):                                #O(n)
            array.append(head.val)
            head = head.next
        return self.is_array_palindrome(array)
        
    def is_array_palindrome(self, array):                   # O(n)
        for i in range(len(array)):
            if array[i] != array[len(array) - 1 - i]:
                return False
        return True
