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

    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #1. Get the mid point of linked list
        #2. Reverse the second half of ll
        #3. Step through the reverse of second half and check first half.
        #4. If all match, then true, other wise false.
        mid = self.get_mid_of_ll(head)
        head2 = self.reverse_ll(mid)
        while head2:
            if head2.val != head.val:
                return False
            head2 = head2.next
            head = head.next
        return True

    def get_mid_of_ll(self,head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse_ll(self,head):
        reverse = ListNode()
        while head:
            reverse.val = head.val
            reverse = ListNode(None, reverse)
            head = head.next
        return reverse.next
